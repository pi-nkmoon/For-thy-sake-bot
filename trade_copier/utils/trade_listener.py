# utils/trade_listener.py

import threading
import logging
from binance.client import Client
from binance.websockets import BinanceSocketManager
from trade_executer import execute_trade
from config import TRADING_PAIR

logger = logging.getLogger(__name__)

class TradeListener:
    def __init__(self, client: Client):
        self.client = client
        self.bm = BinanceSocketManager(self.client)
        self.conn_key = None

    def start(self):
        logger.info("Starting trade listener.")
        self.conn_key = self.bm.start_user_socket(self.process_message)
        self.bm.start()

    def stop(self):
        logger.info("Stopping trade listener.")
        if self.conn_key:
            self.bm.stop_socket(self.conn_key)
        self.bm.close()

    def process_message(self, msg):
        if msg['e'] == 'executionReport':
            symbol = msg['s']
            if symbol == TRADING_PAIR and msg['X'] == 'FILLED':
                side = msg['S']  # 'BUY' or 'SELL'
                order_type = msg['o']  # Order type: 'MARKET', 'LIMIT', etc.
                quantity = float(msg['l'])  # Quantity of last filled trade
                price = float(msg['L'])  # Price of last filled trade
                logger.info(f"Detected trade: {side} {quantity} {symbol} at {price}")

                # Execute the same trade on the target account
                execute_trade(side, quantity, price)