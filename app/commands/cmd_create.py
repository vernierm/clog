from app.util.logging import initialize_log_file


def cmd_create(file_name):
    assert file_name is not None, 'file name not provided, see \'clog create -h\''
    initialize_log_file(file_name)
