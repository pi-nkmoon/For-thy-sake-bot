# app.py

from flask import Flask, render_template, request
from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.spot_trade_model import SpotTrade
from models.futures_trade_model import FuturesTrade
from utils.data_fetcher import fetch_spot_trades, fetch_futures_trades
from utils.data_processor import process_spot_trades, process_futures_trades
import pandas as pd

app = Flask(__name__)

# Setup the database
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables
SpotTrade.metadata.create_all(engine)
FuturesTrade.metadata.create_all(engine)

def update_spot_trades():
    # Fetch and process spot trades
    spot_df = fetch_spot_trades()
    spot_df = process_spot_trades(spot_df)
    
    # Prepare data for insertion
    trades_records = spot_df.to_dict(orient='records')
    
    # Clear existing spot trades
    session.query(SpotTrade).delete()
    
    # Insert new spot trades
    for record in trades_records:
        trade = SpotTrade(
            trade_id=record['trade_id'],
            order_id=record['orderId'],
            symbol=record['symbol'],
            side=record['side'],
            price=record['price'],
            qty=record['qty'],
            quote_qty=record.get('quoteQty'),
            commission=record.get('commission'),
            commission_asset=record.get('commissionAsset'),
            time=record['time']
        )
        session.add(trade)
    session.commit()

def update_futures_trades():
    # Fetch and process futures trades
    futures_df = fetch_futures_trades()
    futures_df = process_futures_trades(futures_df)
    
    # Prepare data for insertion
    trades_records = futures_df.to_dict(orient='records')
    
    # Clear existing futures trades
    session.query(FuturesTrade).delete()
    
    # Insert new futures trades
    for record in trades_records:
        trade = FuturesTrade(
            trade_id=record['trade_id'],
            order_id=record['orderId'],
            symbol=record['symbol'],
            side=record['side'],  # 'LONG' or 'SHORT'
            price=record['price'],
            qty=record['qty'],
            realized_pnl=record.get('realizedPnl'),
            commission=record.get('commission'),
            commission_asset=record.get('commissionAsset'),
            time=record['time']
        )
        session.add(trade)
    session.commit()

@app.route('/', methods=['GET'])
def dashboard():
    update_spot_trades()
    update_futures_trades()
    
    # Get filter parameters from query string
    trade_type_filter = request.args.get('trade_type', 'All')
    side_filter = request.args.get('side', 'All')
    
    # Query spot and futures trades separately
    spot_query = session.query(SpotTrade)
    futures_query = session.query(FuturesTrade)
    
    if trade_type_filter in ['All', 'Spot']:
        if side_filter != 'All':
            spot_query = spot_query.filter(SpotTrade.side == side_filter)
        spot_trades = spot_query.order_by(SpotTrade.time.desc()).all()
    else:
        spot_trades = []
    
    if trade_type_filter in ['All', 'Futures']:
        if side_filter != 'All':
            futures_query = futures_query.filter(FuturesTrade.side == side_filter)
        futures_trades = futures_query.order_by(FuturesTrade.time.desc()).all()
    else:
        futures_trades = []
    
    return render_template(
        'dashboard.html',
        spot_trades=spot_trades,
        futures_trades=futures_trades,
        trade_type_filter=trade_type_filter,
        side_filter=side_filter
    )

if __name__ == '__main__':
    app.run(debug=True)