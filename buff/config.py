# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Source account API keys (the account you're copying from)
SOURCE_API_KEY = 'VLDU11Ftu8KLTb8Jk6y3AFKG7H9d2LMqgftdfUy2yFzmQdh0FHnqZeJJhpbFJDlP'
SOURCE_API_SECRET = 'TWLaKmCH4uquokYAraroV6lhyDaDfvBRhfffc7B0ScsiUnx1g4of1z8qCs5bNGkk'

# Target account API keys (the account you're copying to)
TARGET_API_KEY = os.getenv('TARGET_BINANCE_API_KEY')
TARGET_API_SECRET = os.getenv('TARGET_BINANCE_API_SECRET')

# Trading pair
TRADING_PAIR = 'BTCUSDT'

# Symbol precision settings (these should match Binance's specifications)
PRICE_PRECISION = 2
QUANTITY_PRECISION = 6

# Logging settings
LOG_FILE = 'logs/trade_copier.log'