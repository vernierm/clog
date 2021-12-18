import json
from os import path

TITLE = 'title'


def initialize_log_file(file_path):
    assert not path.exists(file_path), 'file already exists: {}'.format(file_path)
    title = path.basename(file_path)
    data = {
        TITLE: title
    }
    with open(file_path, "w") as f:
        json.dump(data, f)
    print('initialized log file: {}'.format(title))
