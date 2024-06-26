import logging
import logging.handlers
from os import makedirs
from pathlib import Path

CONFIG_FOLDER = Path.cwd()
LOG_FILE = CONFIG_FOLDER / "my_app_log.log"

LEVELS = {
    0: logging.DEBUG,
    1: logging.INFO,
    2: logging.WARNING,
    3: logging.ERROR
}

def create_logger(logger_name: str, level: int) -> logging.Logger:
    # Create needed folder if it doesn't exist
    if not CONFIG_FOLDER.exists():
        makedirs(CONFIG_FOLDER, exist_ok=True)

    logger = logging.getLogger(logger_name)

    logger.setLevel(LEVELS.get(level, 1))

    handler_stream = logging.StreamHandler()
    handler_file = logging.FileHandler(LOG_FILE)
    
    formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
    handler_stream.setFormatter(formatter)
    handler_file.setFormatter(formatter)
    
    # Add the handlers if not present already
    if not any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers):
        logger.addHandler(handler_stream)
    
    if not any(isinstance(handler, logging.FileHandler) and handler.baseFilename == LOG_FILE for handler in logger.handlers):
        logger.addHandler(handler_file)

    return logger


def reset_log_file() -> None:
    if Path(LOG_FILE).exists():
        with open(LOG_FILE, 'w') as f:
            f.write('')
