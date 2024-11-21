import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s : %(message)s]"

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_dir ="logs"
chdir = os.chdir(os.path.join("..", ".."))
log_filepath = os.path.join(os.getcwd(),log_dir, LOG_FILE)
os.makedirs(os.path.dirname(log_filepath), exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)

    ]
)

logger = logging.getLogger("MLproject")