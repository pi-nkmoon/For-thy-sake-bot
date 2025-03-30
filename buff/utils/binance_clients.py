# utils/binance_clients.py

from binance.client import Client
from binance.websockets import BinanceSocketManager
from config import SOURCE_API_KEY, SOURCE_API_SECRET, TARGET_API_KEY, TARGET_API_SECRET

def get_source_client():
    return Client(api_key=SOURCE_API_KEY, api_secret=SOURCE_API_SECRET)

def get_target_client():
    return Client(api_key=TARGET_API_KEY, api_secret=TARGET_API_SECRET)

def get_binance_socket_manager(client):
    return BinanceSocketManager(client)