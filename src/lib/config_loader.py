import argparse
import yaml


def load_config():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--config", dest="config", required=True)
    args = arg_parser.parse_args()
    return yaml.safe_load(open(args.config))
