import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', 
                        default='stylish', 
                        help='set format of output')
    
    return parser.parse_args()
    
    
    if __name__ == "__main__":
        main()