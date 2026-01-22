import os
from dotenv import load_dotenv
from app.core.logger import get_logger

log = get_logger("core.env")

load_dotenv()


def get_env(key: str) -> str:
    value = os.getenv(key)

    if value is None:
        raise RuntimeError(f"Missing environment variable: {key}")

    log.debug("Loaded env var: %s", key)
    return value
