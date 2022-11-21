from PmBlocker import ubot
from PmBlocker.modules import ALL_MODULES
from PmBlocker.logger import LOGGER


if __name__ == "__main__":
    ubot.start()
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    ubot.send_message(ubot.get_me().id, "Pm Blocker Initialized")
