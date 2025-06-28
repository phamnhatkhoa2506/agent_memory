import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/agent_memory.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


