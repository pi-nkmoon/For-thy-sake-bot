# utils/trade_poller.py

import time
import logging
from binance.client import Client
from new_utils.trade_executor import execute_trade
from config import TRADING_PAIR, POLLING_INTERVAL
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

class TradePoller:
    def __init__(self, source_client: Client):
        self.source_client = source_client
        self.last_trade_id = None  # Keep track of the last processed trade ID

    def start(self):
        logger.info("Starting trade poller.")
        while True:
            self.poll_trades()
            time.sleep(POLLING_INTERVAL)

    def poll_trades(self):
        try:
            # Fetch recent trades
            trades = self.source_client.futures_account_trades(symbol=TRADING_PAIR)
            if not trades:
                logger.debug("No trades found.")
                return

            # Sort trades by time
            trades.sort(key=lambda x: x['time'])

            # Find new trades since last processed trade
            new_trades = []
            for trade in trades:
                trade_id = trade['id']
                if self.last_trade_id is None or trade_id > self.last_trade_id:
                    new_trades.append(trade)

            if new_trades:
                logger.info(f"Found {len(new_trades)} new trade(s).")
                # Process new trades
                for trade in new_trades:
                    self.process_trade(trade)
                # Update the last_trade_id to the most recent trade ID
                self.last_trade_id = new_trades[-1]['id']
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: {e}")
        except BinanceRequestException as e:
            logger.error(f"Binance Request Exception: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")

    def process_trade(self, trade):
        side = trade['side']  # 'BUY' or 'SELL'
        quantity = float(trade['qty'])
        logger.info(f"Processing trade ID {trade['id']}: {side} {quantity} {TRADING_PAIR}")
        # Execute the same trade on the target account
        execute_trade(side, quantity)