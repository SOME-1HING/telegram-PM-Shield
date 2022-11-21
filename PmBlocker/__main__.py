import asyncio

from PmBlocker import ubot, UB_ID
from PmBlocker.modules import ALL_MODULES
from PmBlocker.logger import LOGGER


async def load_start():

    await ubot.send_message(UB_ID, "Pm Blocker Initialized")

    return


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    LOGGER.info("[INFO]: STARTED")
    ubot.loop.run_until_complete(load_start())
