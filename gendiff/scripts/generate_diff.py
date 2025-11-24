import json
import yaml

def load_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        if file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(f)
        return json.load(f)

def generate_diff(file_path1, file_path2, format_name='stylish'):
    
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    def build_diff(dict1, dict2):
        keys = sorted(dict1.keys() | dict2.keys())
        diff = []

        for key in keys:
            if key not in dict1:
                diff.append(f"  + {key}: {dict2[key]}")
            elif key not in dict2:
                diff.append(f"  - {key}: {dict1[key]}")
            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested = build_diff(dict1[key], dict2[key])
                diff.append(f"    {key}: {{\n{nested}\n    }}")
            elif dict1[key] != dict2[key]:
                diff.append(f"  - {key}: {dict1[key]}")
                diff.append(f"  + {key}: {dict2[key]}")
            else:
                diff.append(f"    {key}: {dict1[key]}")
        return '\n'.join(diff)

    diff_result = build_diff(data1, data2)
    
    return '{\n' + diff_result + '\n}'


def format_value(value):
    
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value if isinstance(value, (int, float)) else str(value)