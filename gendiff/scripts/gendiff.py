import argparse
import json


def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', help='set format of output')
    
    args = parser.parse_args()
    
    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)
    print("Data from first_file.json:")
    print(json.dumps(data1, indent=2))

    print("\nData from second_file.json:")
    print(json.dumps(data2, indent=2))