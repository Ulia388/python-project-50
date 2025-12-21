def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
        

def plain(data, parent=''):
    lines = []

    for node in data:
        key = node['key']
        type_ = node['type']
        value = node.get('value')
        children = node.get('children', [])
        full_key = f'{parent}.{key}' if parent else key

        if type_ == 'added':
            value = format_value(value)
            lines.append(
                f"Property '{full_key}' was added with value: {value}"
            )
        elif type_ == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif type_ == 'changed':
            old = format_value(value['old'])
            new = format_value(value['new'])
            lines.append(
                f"Property '{full_key}' was updated. From {old} to {new}"
            )
        elif type_ == 'nested':
            nested_str = plain(children, parent=full_key)
            lines.append(nested_str)

    return "\n".join(lines)


def format_plain(data):
    return plain(data)