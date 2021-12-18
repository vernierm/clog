import glob
import json
from os import path

from app.util.const import BASE_DIR_PATH

JSON_EXTENSION = '.json'
TITLE = 'title'


def initialize_log_file(file_name):
    file_path = path.join(BASE_DIR_PATH, file_name + JSON_EXTENSION)
    assert not path.exists(file_path), 'file already exists: {}'.format(file_path)

    title = file_basename(file_path)
    data = {
        TITLE: title
    }

    with open(file_path, "w") as f:
        json.dump(data, f)
    print('initialized log file: {}'.format(title))


def list_log_file_names():
    return [file_basename(f) for f in glob.glob(BASE_DIR_PATH + '/*.json')]


def file_basename(file_path):
    basename = path.basename(file_path)
    return path.splitext(basename)[0]
