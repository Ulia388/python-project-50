import argparse
import os
import yaml
import json


def read_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    with open(filepath, 'r') as file:
        if ext in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}")


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', help='set format of output')
    
    args = parser.parse_args()
    
    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)
    print("Data from first_file.json:")
    print(json.dumps(data1, indent=2))

    print("\nData from second_file.json:")
    print(json.dumps(data2, indent=2))