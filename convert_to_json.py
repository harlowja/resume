import argparse
import json

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File to convert",
                        required=True, dest='file')
    args = parser.parse_args()

    y_path = args.file
    with open(y_path, 'rb') as fh:
        y_contents = fh.read()
        y_data = yaml.safe_load(y_contents)
    print(json.dumps(y_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
