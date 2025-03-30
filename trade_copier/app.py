# app.py

import logging
from utils.binance_clients import get_source_client
from utils.trade_listener import TradeListener
from config import LOG_FILE

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Trade Copier Application.")

    source_client = get_source_client()
    trade_listener = TradeListener(source_client)

    try:
        trade_listener.start()
        logger.info("Trade Listener started. Press Ctrl+C to stop.")
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        logger.info("Interrupted by user.")
    finally:
        trade_listener.stop()
        logger.info("Trade Copier Application stopped.")

if __name__ == "__main__":
    main()