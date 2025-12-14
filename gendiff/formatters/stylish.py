INDENT_STEP = 4


def make_indent(depth, prefix_len=0):
    
    return ' ' * (INDENT_STEP * depth - prefix_len)


def format_value(value, depth=1):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = ['{']
        indent = ' ' * (INDENT_STEP * (depth + 1))
        for k in sorted(value.keys()):
            v = value[k]
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append(' ' * (INDENT_STEP * depth) + '}')
        return "\n".join(lines)
    else:
        return str(value)


def stylish(node, depth=1):
    lines = []
    indent = make_indent(depth - 1)
    for item in sorted(node, key=lambda x: x['key']):
        key = item['key']
        type_ = item['type']
        value = item.get('value')
        children = item.get('children', [])
        formatted_value = format_value(value, depth)
        if type_ == 'added':
            lines.append(
                f"{make_indent(depth, 2)}+ {key}: {formatted_value}"
            )
        elif type_ == 'removed':
            lines.append(
                f"{make_indent(depth, 2)}- {key}: {formatted_value}"
            )
        elif type_ == 'unchanged':
            lines.append(
                f"{make_indent(depth, 2)}  {key}: {formatted_value}"
            )
        elif type_ == 'changed':
            old_value = item['value']['old']
            new_value = item['value']['new']
            lines.append(
                f"{make_indent(depth, 2)}- {key}: "
                f"{format_value(old_value, depth)}"
            )
            lines.append(
                f"{make_indent(depth, 2)}+ {key}: "
                f"{format_value(new_value, depth)}"
            )
        elif type_ == 'nested':
            nested = stylish(children, depth + 1)
            lines.append(f"{make_indent(depth, 2)}  {key}: {nested}")
    return f"{{\n{'\n'.join(lines)}\n{indent}}}"


def format_stylish(data):
    return stylish(data, depth=1)