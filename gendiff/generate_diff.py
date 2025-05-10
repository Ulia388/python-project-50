import json


def generate_diff(file_path1, file_path2):
  
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    lines = ['{']

    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key in data1 and key not in data2:
            
            lines.append(f"  - {key}: {format_value(val1)}")
        elif key not in data1 and key in data2:
            
            lines.append(f"  + {key}: {format_value(val2)}")
        else:
            
            if val1 == val2:
                
                lines.append(f"    {key}: {format_value(val1)}")
            else:
                
                lines.append(f"  - {key}: {format_value(val1)}")
                lines.append(f"  + {key}: {format_value(val2)}")

    lines.append('}')
    return '\n'.join(lines)


def format_value(value):
    
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value if isinstance(value, (int, float)) else str(value)