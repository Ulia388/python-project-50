from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain import format_plain 
from gendiff.formatters.stylish import format_stylish


def formatters_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")
    