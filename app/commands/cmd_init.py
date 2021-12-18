import os
from os import path

from app.commands.logging import initialize_log_file
from app.const import COMMON, HOME, BASE_DIR


def cmd_init(args):
    base_dir_path = path.join(HOME, BASE_DIR)
    os.makedirs(base_dir_path, exist_ok=True)
    print('initialized base dir: {}'.format(base_dir_path))
    common_file_path = path.join(base_dir_path, COMMON)
    initialize_log_file(common_file_path)
