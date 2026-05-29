try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
except ModuleNotFoundError:  # keeps local demo/tests working before pip install
    MongoClient = None
    PyMongoError = Exception

from src.common.settings import get_settings
from src.common.logger import get_logger

logger = get_logger(__name__)


def get_database():
    settings = get_settings()
    if MongoClient is None:
        logger.warning("pymongo not installed, API will use in-memory fallback.")
        return None
    try:
        client = MongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=1500)
        client.admin.command("ping")
        return client[settings.mongodb_db]
    except PyMongoError as exc:
        logger.warning("MongoDB unavailable, API will use in-memory fallback. Error: %s", exc)
        return None
