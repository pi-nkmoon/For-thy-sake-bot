import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite://///Users/mihirchaturvedi/for_thy_sake_bot/trading_monitor/data/trades.db'

API_KEY = 'VLDU11Ftu8KLTb8Jk6y3AFKG7H9d2LMqgftdfUy2yFzmQdh0FHnqZeJJhpbFJDlP'
API_SECRET ='TWLaKmCH4uquokYAraroV6lhyDaDfvBRhfffc7B0ScsiUnx1g4of1z8qCs5bNGkk'


SYMBOLS = ['BTCUSDT']  

DATA_DIR = os.path.join(BASE_DIR, 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)



