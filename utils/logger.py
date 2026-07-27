import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("PlaywrightFramework")

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/automation.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)