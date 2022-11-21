import os

STRING_SESSION = str(os.environ.get("STRING_SESSION", None))
API_ID = int(os.environ.get("API_ID", None))
API_HASH = str(os.environ.get("API_HASH", None))
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
