import logging
import os
import sys

log_dir = "logs"
log_formate = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_formate,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("empWellness")
