def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
        

def plain(tree):
    lines = []

    for node in tree:
        key = node['key']
        type_ = node['type']
        value = node.get('value')

        if type_ == 'added':
            lines.append(
                f"Key '{key}' was added with value: {format_value(value)}"
            )
        elif type_ == 'removed':
            lines.append(f"Key '{key}' was removed")
        elif type_ == 'changed':
            old = format_value(value['old'])
            new = format_value(value['new'])
            lines.append(f"Key '{key}' was updated. From {old} to {new}")
        elif type_ == 'nested':
            nested_str = plain(node['children'])
            lines.append(
                f"Key '{key}' contains nested structure:\n{nested_str}"
            )

    return "\n".join(lines)


def format_plain(data):
    return plain(data)