#!/usr/bin/env python
import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, format=args.format)
    print(diff)


if __name__ == '__main__':
    main()
