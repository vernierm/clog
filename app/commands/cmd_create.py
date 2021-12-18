from app.util.file_util import assert_base_dir_exists
from app.util.logging import initialize_log_file


def cmd_create(file_name):
    assert file_name is not None, 'file name not provided, see \'clog create -h\''
    assert_base_dir_exists()
    initialize_log_file(file_name)
