import logging

from deployment_model.config import config
from deployment_model.config import logging_config

VERSION_PATH = config.ROOT_DIR / 'VERSION'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False

with open(VERSION_PATH, 'r') as version:
	__version__ = version.read().strip()