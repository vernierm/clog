from app.util.logging import list_log_file_names


def cmd_ls():
    files = list_log_file_names()
    print(*files, sep='\n')
