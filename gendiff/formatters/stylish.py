def format_value(value, depth=1):
    indent = '  ' * depth
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}  {k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    else:
        return str(value)


def stylish(node, level=2):
    indent = '  ' * level
    lines = []

    for item in node:
        key = item['key']
        type_ = item['type']
        value = item.get('value')
        children = item.get('children', [])

        if type_ == 'added':
            lines.append(f"{indent}  + {key}: {format_value(value, level)}")
        elif type_ == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(value, level)}")
        elif type_ == 'unchanged':
            lines.append(f"{indent}    {key}: {format_value(value, level)}")
        elif type_ == 'changed':
            old_value = item['value']['old']
            new_value = item['value']['new']
            lines.append(f"{indent}  - {key}: {format_value(old_value, level)}")
            lines.append(f"{indent}  + {key}: {format_value(new_value, level)}")
        elif type_ == 'nested':
            nested = stylish(children, level + 1)
            lines.append(f"{indent}    {key}: {{\n{nested}\n{indent}    }}")
    return "\n".join(lines)
    

def format_stylish(data):
    return stylish(data)