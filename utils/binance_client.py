
# utils/binance_client.py

from binance.client import Client
from config import API_KEY, API_SECRET

def get_client():
    if not API_KEY or not API_SECRET:
        raise ValueError("API Key or Secret not found. Please set your environment variables.")
    return Client(api_key=API_KEY, api_secret=API_SECRET)