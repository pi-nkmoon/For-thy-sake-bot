# models/futures_trade_model.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FuturesTrade(Base):
    __tablename__ = 'futures_trades'

    trade_id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    symbol = Column(String(20))
    side = Column(String(10))  # 'LONG' or 'SHORT'
    price = Column(Float)
    qty = Column(Float)
    realized_pnl = Column(Float, nullable=True)
    commission = Column(Float, nullable=True)
    commission_asset = Column(String(10), nullable=True)
    time = Column(DateTime)

    def __repr__(self):
        return f"<FuturesTrade(id={self.trade_id}, symbol={self.symbol}, side={self.side}, price={self.price})>"