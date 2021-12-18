from app.util.file_util import list_log_file_names, assert_base_dir_exists


def cmd_ls():
    assert_base_dir_exists()
    files = list_log_file_names()
    print(*files, sep='\n')
