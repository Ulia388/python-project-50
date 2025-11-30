import json
import os

import yaml


def file_format(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.yaml', '.yml']:
        return 'yaml'
    elif ext == '.json':
        return 'json'


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def data_format(data, format):
    if format == 'json':
        return json.loads(data)
    elif format == 'yml' or format == 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError(f'Unsupported file format: {format}')  


def parser_file(file_path):
    format = file_format(file_path)
    data = read_file(file_path)
    return data_format(data, format) 
