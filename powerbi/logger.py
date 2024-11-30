import logging
from logging.handlers import RotatingFileHandler
import os

# Define logging format and log file path
LOG_FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = os.getenv("LOG_FILE", f"{os.path.abspath(os.getcwd())}/log/powerbi_api.log")  # Default log file

def get_logger(name: str):
    """Create and configure a logger."""
    logger = logging.getLogger(name)

    if not logger.hasHandlers():  # Prevent duplicate handlers
        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(LOG_FORMAT)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # Rotating file handler
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5  # 5 MB per file, 5 backups
        )
        file_formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Set logging level
        logger.setLevel(LOG_LEVEL)
    return logger