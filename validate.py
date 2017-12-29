import argparse
import json
import logging

from jsonschema import validate
import requests
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", '--file',
                        help="File to load & validate",
                        required=True, dest='file')
    parser.add_argument("-v", '--verbose', help="Increase verbosity",
                        action='count', dest='verbosity', default=0)
    args = parser.parse_args()

    if args.verbosity >= 1:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    r_path = args.file
    if r_path.endswith(".json"):
        r_loader = json.loads
    else:
        r_loader = yaml.safe_load
    with open(r_path, 'rb') as fh:
        r_contents = fh.read()
        r_data = r_loader(r_contents)
        s_url = r_data['meta']['canonical']
        s_resp = requests.get(s_url)
        s_resp.raise_for_status()
        s_data = s_resp.json()
        validate(r_data, s_data)


if __name__ == '__main__':
    main()
