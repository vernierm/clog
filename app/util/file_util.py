import glob
import json
from os import path

from app.util.const import BASE_DIR_PATH

JSON_EXTENSION = '.json'


def list_log_file_names():
    return [file_basename(f) for f in glob.glob(BASE_DIR_PATH + '/*' + JSON_EXTENSION)]


def assert_not_exists(file_path):
    assert not path.exists(file_path), 'file already exists: {}'.format(file_path)


def assert_exists(file_path):
    assert path.exists(file_path), 'file does not exist: {}'.format(file_path)


def prepare_file_path(file_name):
    return path.join(BASE_DIR_PATH, file_name + JSON_EXTENSION)


def file_basename(file_path):
    basename = path.basename(file_path)
    return path.splitext(basename)[0]


def dump_to_file(file_path, json_data):
    with open(file_path, 'w') as f:
        json.dump(json_data, f)


def read_json_from_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
