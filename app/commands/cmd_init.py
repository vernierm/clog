import os

from app.util.const import COMMON, BASE_DIR_PATH
from app.util.logging import initialize_log_file


def cmd_init():
    os.makedirs(BASE_DIR_PATH, exist_ok=True)
    print('initialized base dir: {}'.format(BASE_DIR_PATH))
    initialize_log_file(COMMON)
