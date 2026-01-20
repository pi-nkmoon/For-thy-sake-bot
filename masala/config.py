# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Source account API keys (the account you're copying from)
SOURCE_API_KEY = 'source api key'
SOURCE_API_SECRET = 'source api secret key'

# Target account API keys (the account you're copying to)
TARGET_API_KEY = 'Target api key'
TARGET_API_SECRET = 'Target api secret key'

# Trading pair
TRADING_PAIR = 'ETHUSDT'

# Symbol precision settings (these should match Binance's specifications)

QUANTITY_PRECISION = 6

# Logging settings
LOG_FILE = os.path.join('logs', 'trade_copier.log')

POLLING_INTERVAL = 1  # 1 second
