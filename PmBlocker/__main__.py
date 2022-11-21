import asyncio

from PmBlocker import ubot, UB_ID
from PmBlocker.modules import ALL_MODULES
from PmBlocker.logger import LOGGER


async def load_start():

    await ubot.send_message(UB_ID, "Pm Blocker Initialized")

    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    LOGGER.info("[INFO]: STARTED")


loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())
