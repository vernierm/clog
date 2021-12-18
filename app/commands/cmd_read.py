from app.util.file_util import assert_base_dir_exists, assert_exists, prepare_file_path
from app.util.logging import print_logs_from_file


def cmd_read(name):
    assert name is not None, 'file name should be specified when using \'-n\' flag'
    assert_base_dir_exists()
    file_path = prepare_file_path(name)
    assert_exists(file_path)
    print_logs_from_file(name)
