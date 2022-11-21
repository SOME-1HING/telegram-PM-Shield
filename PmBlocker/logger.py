import logging

FORMAT = "[PmBLocker] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("pm_blocker_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
    logging.WARNING
)

LOGGER = logging.getLogger("[PmBLocker]")
LOGGER.info("PmBLocker is starting.")
