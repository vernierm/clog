from app.util.file_util import prepare_file_path, assert_not_exists, file_basename, assert_exists, dump_to_file, \
    read_json_from_file

LOGS = 'logs'
TITLE = 'title'


def initialize_log_file(file_name):
    file_path = prepare_file_path(file_name)
    assert_not_exists(file_path)

    title = file_basename(file_path)
    json_data = {
        TITLE: title,
        LOGS: []
    }

    dump_to_file(file_path, json_data)
    print('initialized log file: {}'.format(title))


def append_to_file(file_name, text):
    file_path = prepare_file_path(file_name)
    assert_exists(file_path)
    json_data = read_json_from_file(file_path)
    json_data[LOGS].append(text)
    dump_to_file(file_path, json_data)


def print_logs_from_file(file_name):
    file_path = prepare_file_path(file_name)
    assert_exists(file_path)
    json_data = read_json_from_file(file_path)
    print(*json_data[LOGS], sep='\n')
