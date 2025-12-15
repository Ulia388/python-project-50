from gendiff.formatters.json import format_json
from gendiff.scripts.build_diff import build_diff
from gendiff.scripts.parser import parser_file


def generate_diff(file_path1, file_path2, formatter='stylish'):
  
    data1 = parser_file(file_path1)
    data2 = parser_file(file_path2)
    diff_result = build_diff(data1, data2)

    return format_json(diff_result)
