import logging
import os

log_dir = ".src/logging"
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=os.path.join(log_dir, 'app.log'),
    filemode='a'
)

logger = logging.getLogger(__name__)

def log_message(level, message):
    getattr(logger, level)(f"[{level}] {message}")