# utils/trade_executor.py

import logging
from binance.client import Client
from config import TARGET_API_KEY, TARGET_API_SECRET, TRADING_PAIR
from binance.enums import SIDE_BUY, SIDE_SELL
from binance.exceptions import BinanceAPIException, BinanceOrderException
import math

logger = logging.getLogger(__name__)

def execute_trade(side, quantity):
    client = Client(api_key=TARGET_API_KEY, api_secret=TARGET_API_SECRET)
    try:
        # Fetch symbol info to get quantity precision
        exchange_info = client.futures_exchange_info()
        symbol_info = next(filter(lambda x: x['symbol'] == TRADING_PAIR, exchange_info['symbols']), None)

        if symbol_info:
            lot_size_filter = next(filter(lambda x: x['filterType'] == 'LOT_SIZE', symbol_info['filters']), None)
            if lot_size_filter:
                step_size = float(lot_size_filter['stepSize'])
                # Adjust quantity precision
                quantity = round_quantity(quantity, step_size)
            else:
                logger.error(f"LOT_SIZE filter not found for {TRADING_PAIR}.")
                return
        else:
            logger.error(f"Symbol information for {TRADING_PAIR} not found.")
            return

        # Place a market order
        if side == 'BUY':
            order = client.futures_create_order(
                symbol=TRADING_PAIR,
                side=SIDE_BUY,
                type='MARKET',
                quantity=quantity
            )
        elif side == 'SELL':
            order = client.futures_create_order(
                symbol=TRADING_PAIR,
                side=SIDE_SELL,
                type='MARKET',
                quantity=quantity
            )
        else:
            logger.error(f"Unknown side: {side}")
            return

        logger.info(f"Executed {side} order on target account: {order}")
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
    except BinanceOrderException as e:
        logger.error(f"Binance Order Exception: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def round_quantity(quantity, step_size):
    precision = int(round(-math.log(step_size, 10), 0))
    return float(round(quantity - (quantity % step_size), precision))