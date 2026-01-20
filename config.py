import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite://///Users/mihirchaturvedi/for_thy_sake_bot/trading_monitor/data/trades.db'

API_KEY = 'api key'
API_SECRET ='api secret key'


SYMBOLS = ['BTCUSDT']  

DATA_DIR = os.path.join(BASE_DIR, 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)



