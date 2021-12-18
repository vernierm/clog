from app.util.file_util import list_log_file_names


def cmd_ls():
    files = list_log_file_names()
    print(*files, sep='\n')
