# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Source account API keys (the account you're copying from)
SOURCE_API_KEY = 'VLDU11Ftu8KLTb8Jk6y3AFKG7H9d2LMqgftdfUy2yFzmQdh0FHnqZeJJhpbFJDlP'
SOURCE_API_SECRET = 'TWLaKmCH4uquokYAraroV6lhyDaDfvBRhfffc7B0ScsiUnx1g4of1z8qCs5bNGkk'

# Target account API keys (the account you're copying to)
TARGET_API_KEY = 'Hi1ZpW3oBNH991nA8As1hCxxetiLHB1p9aFiJkboA6V4eCJ9Eb2bnZpJhU3GFax8'
TARGET_API_SECRET = 'COW1SfTxvWOHchhb4o8ASSO5x07QVlzTIPjA08WYwyPumr2qDqjUv8KS39UDnBsr'

# Trading pair
TRADING_PAIR = 'ETHUSDT'

# Symbol precision settings (these should match Binance's specifications)

QUANTITY_PRECISION = 6

# Logging settings
LOG_FILE = os.path.join('logs', 'trade_copier.log')

POLLING_INTERVAL = 1  # 1 second