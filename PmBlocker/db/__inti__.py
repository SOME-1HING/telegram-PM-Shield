import asyncio
import sys

from motor.motor_asyncio import AsyncIOMotorClient as async_mongo
from pymongo.errors import ServerSelectionTimeoutError

from PmBlocker.logger import LOGGER
from ..config import MONGO_DB_URI

LOGGER.info("[PmBlocker]: INITIALIZING DATABASE")
async_mongo_client = async_mongo(MONGO_DB_URI)
db = async_mongo_client.PmBlocker

try:
    asyncio.get_event_loop().run_until_complete(async_mongo_client.server_info())
    LOGGER.info("Mongo Server is alive")
except ServerSelectionTimeoutError:
    sys.exit(LOGGER.critical("Can't connect to mongodb! Exiting..."))
