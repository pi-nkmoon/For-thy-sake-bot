# test_fetch_futures_trades.py

from binance.client import Client
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = 'VLDU11Ftu8KLTb8Jk6y3AFKG7H9d2LMqgftdfUy2yFzmQdh0FHnqZeJJhpbFJDlP'
API_SECRET = 'TWLaKmCH4uquokYAraroV6lhyDaDfvBRhfffc7B0ScsiUnx1g4of1z8qCs5bNGkk'

print(f"API_KEY is set: {bool(API_KEY)}")
print(f"API_SECRET is set: {bool(API_SECRET)}")

client = Client(api_key=API_KEY, api_secret=API_SECRET)

try:
    trades = client.futures_account_trades(symbol='BTCUSDT')
    df = pd.DataFrame(trades)
    print(f"Fetched {len(df)} futures trades.")
    if not df.empty:
        print(df.head())
    else:
        print("No futures trades found.")
except Exception as e:
    print(f"Error fetching futures trades: {e}")