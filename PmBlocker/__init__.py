from pyrogram import Client
import os
from PmBlocker.config import *  # if config is added vro
import time

START_TIME = time.time()

ubot = Client(
    ":memory:",
    session_string=STRING_SESSION,
    in_memory=True,
    api_id=os.environ.get("API_ID"),
    api_hash=os.environ["API_HASH"],
)
