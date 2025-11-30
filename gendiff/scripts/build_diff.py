
def build_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff_tree = []

    for key in keys:
        in_dict1 = key in dict1
        in_dict2 = key in dict2

        if in_dict1 and not in_dict2:
            diff_tree.append({
                'key': key,
                'type': 'removed',
                'value': dict1[key]
            })
        elif not in_dict1 and in_dict2:
            diff_tree.append({
                'key': key,
                'type': 'added',
                'value': dict2[key]
            })
        else:
            val1 = dict1[key]
            val2 = dict2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                
                children = build_diff(val1, val2)
                diff_tree.append({
                    'key': key,
                    'type': 'nested',
                    'children': children
                })
            elif val1 == val2:
                diff_tree.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': val1
                })
            else:
                
                diff_tree.append({
                    'key': key,
                    'type': 'changed',
                    'value': {
                        'old': val1,
                        'new': val2
                    }
                })

    return diff_tree