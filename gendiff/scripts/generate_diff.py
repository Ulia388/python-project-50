#!/usr/bin/env python3

import argparse

from gendiff.generate_diff import generate_diff


def main():

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('file_path1', help='Path to the first file')
    parser.add_argument('file_path2', help='Path to the second file')
    args = parser.parse_args()
    diff = generate_diff(args.file_path1, args.file_path2)
    print(diff)


if __name__ == "__main__":
    main()