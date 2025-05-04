#!/usr/bin/env python3

import argparse
import json

def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', help='set format of output')
    
    args = parser.parse_args()
    # Ваша основная логика здесь
    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)
    print("Data from first_file.json:")
    print(data1)

    print("\nData from second_file.json:")
    print(data2)


if __name__ == "__main__":
    main()



