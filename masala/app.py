# app.py

import logging
import os
from new_utils.binance_clients import get_source_client
from new_utils.trade_poller import TradePoller
from config import LOG_FILE

# Ensure the logs directory exists
logs_dir = os.path.dirname(LOG_FILE)
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

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
    trade_poller = TradePoller(source_client)

    try:
        trade_poller.start()
    except KeyboardInterrupt:
        logger.info("Interrupted by user.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        logger.info("Trade Copier Application stopped.")

if __name__ == "__main__":
    main()