import yaml
import sys
import argparse
import json

parse = argparse.ArgumentParser()
parse.add_argument("filename", help='YAML filename.')
parse.add_argument('-p', '--parameter', help='Input parameters as JSON format.', action='append')

args = parse.parse_args()

if args.parameter is None:
    print("No parameter specified.", file=sys.stderr)
    exit(-1)

try:
    f = open(args.filename, 'r')
    data = yaml.load(f, Loader=yaml.SafeLoader)
    for param in args.parameter:
        try:
            json_obj = json.loads(param)
            data.update(json_obj)
            print(yaml.dump(data))
        except json.JSONDecodeError:
            print("Parameters in invalid format.", file=sys.stderr)
            exit(-1)

    f.close()
except FileNotFoundError:
    print("File not found.", file=sys.stderr)
    exit(-1)
