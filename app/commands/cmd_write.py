from app.util.file_util import assert_base_dir_exists, assert_exists, prepare_file_path
from app.util.logging import append_to_file


def cmd_write(name, text):
    assert name is not None, 'file name should be specified when using \'-n\' flag'
    assert text is not None, 'input text is mandatory'
    assert_base_dir_exists()
    file_path = prepare_file_path(name)
    assert_exists(file_path)
    append_to_file(name, text)
