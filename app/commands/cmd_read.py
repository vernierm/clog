from app.util.logging import print_logs_from_file


def cmd_read(name):
    assert name is not None, 'file name should be specified when using \'-n\' flag'
    print_logs_from_file(name)
