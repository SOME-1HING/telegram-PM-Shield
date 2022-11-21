import asyncio

from PmBlocker import ubot
from PmBlocker.modules import ALL_MODULES
from PmBlocker.logger import LOGGER


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    LOGGER.info("[INFO]: STARTED")
    ubot.run()
