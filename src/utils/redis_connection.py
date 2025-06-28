import os

from redis import Redis
from src.log.logger import logger  # Use relative import; run as a module, not as a script


def connect_redis(url: str) -> Redis | None:
    redis_client = Redis.from_url(url)
    redis_client.ping()

    logger.info("Connect Redis successfully")

    return redis_client

    
REDIS_URL = os.getenv("REDIS_URL")
redis_client = connect_redis(REDIS_URL)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    connect_redis(os.getenv("REDIS_URL"))