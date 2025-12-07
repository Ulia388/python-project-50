INDENT_STEP = 4


def format_value(value, depth=1):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = ['{']
        indent = ' ' * (INDENT_STEP * depth)
        for k, v in value.items():
            lines.append(
                f"{indent}{k}: {format_value(v, depth + 1)}"
            )
        lines.append(' ' * (INDENT_STEP * (depth - 1)) + '}')
        
        return "\n".join(lines)
    else:
        return str(value)


def stylish(node, depth=1):
    indent = ' ' * (INDENT_STEP * (depth - 1))
    lines = []
    
    for item in node:
        key = item['key']
        type_ = item['type']
        value = item.get('value')
        children = item.get('children', [])
        
        if type_ == 'added':
            lines.append(f"{indent}+ {key}: {format_value(value, depth)}")
        elif type_ == 'removed':
            lines.append(f"{indent}- {key}: {format_value(value, depth)}")
        elif type_ == 'unchanged':
            lines.append(f"{indent}  {key}: {format_value(value, depth)}")
        elif type_ == 'changed':
            old_value = item['value']['old']
            new_value = item['value']['new']
            lines.append(f"{indent}- {key}: {format_value(old_value, depth)}")
            lines.append(f"{indent}+ {key}: {format_value(new_value, depth)}")
        elif type_ == 'nested':
            nested = stylish(children, depth + 1)
            lines.append(f"{indent}  {key}: {{\n{nested}\n{indent}  }}")

    result = '\n'.join(lines)
    return f"{result}\n{' ' * (INDENT_STEP * (depth - 1))}"


def format_stylish(data):
    return stylish(data)