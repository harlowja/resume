import json
import sys

from jsonschema import validate
import requests
import yaml

SCHEMA_URL = ('https://raw.githubusercontent.com/jsonresume'
              '/resume-schema/v1.0.0/schema.json')


def main():
    r_path = sys.argv[1]
    if r_path.endswith(".json"):
        r_loader = json.loads
    else:
        r_loader = yaml.safe_load
    with open(r_path, 'rb') as fh:
        r_contents = fh.read()
        r_data = r_loader(r_contents)
        s_resp = requests.get(SCHEMA_URL)
        s_resp.raise_for_status()
        s_data = s_resp.json()
        validate(r_data, s_data)


if __name__ == '__main__':
    main()
