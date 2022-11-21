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

ubot.start()

ub = ubot.get_me()
UB_ID = ub.id
if ub.last_name:
    UB_NAME = ub.first_name + " " + ub.last_name
else:
    UB_NAME = ub.first_name
UB_USERNAME = ub.username
