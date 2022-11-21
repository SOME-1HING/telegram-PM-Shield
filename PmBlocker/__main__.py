import asyncio

from PmBlocker import ubot
from PmBlocker.modules import ALL_MODULES
from PmBlocker.logger import LOGGER


async def load_start():
    ub = await ubot.get_me()

    await ubot.send_message(ub.id, "Pm Blocker Initialized")

    LOGGER.info("[INFO]: STARTED")


if __name__ == "__main__":
    ubot.start()
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(load_start())
    loop.close()
