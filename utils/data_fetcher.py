# utils/data_fetcher.py

from utils.binance_client import get_client
import pandas as pd
from binance.exceptions import BinanceAPIException, BinanceRequestException

def fetch_spot_trades(symbol='BTCUSDT'):
    client = get_client()
    try:
        trades = client.get_my_trades(symbol=symbol)
        df = pd.DataFrame(trades)
        print(f"Fetched {len(df)} spot trades.")
        return df
    except (BinanceAPIException, BinanceRequestException) as e:
        print(f"Error fetching spot trades: {e}")
        return pd.DataFrame()

def fetch_futures_trades(symbol='BTCUSDT'):
    client = get_client()
    try:
        trades = client.futures_account_trades(symbol=symbol)
        df = pd.DataFrame(trades)
        print(f"Fetched {len(df)} futures trades.")
        return df
    except (BinanceAPIException, BinanceRequestException) as e:
        print(f"Error fetching futures trades: {e}")
        return pd.DataFrame()