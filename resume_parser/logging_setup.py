from loguru import logger
import sys

def init_logging(log_file: str = None, level: str = "INFO"):
    logger.remove()
    logger.add(sys.stderr, level=level, backtrace=True, diagnose=True)

    if log_file:
        # Log to file with rotation, optional compression
        logger.add(
            log_file,
            rotation="10 MB",        # rotate after 10MB
            retention="10 days",     # keep 10 days of logs
            compression="zip",       # compress old logs
            level=level,
            backtrace=True,
            diagnose=True,
        )
