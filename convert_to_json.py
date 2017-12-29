import json
import sys

import yaml


def main():
    y_path = sys.argv[1]
    with open(y_path, 'rb') as fh:
        y_contents = fh.read()
        y_data = yaml.safe_load(y_contents)
    print(json.dumps(y_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
