#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
import os
import json
import datetime
import argparse
import pprint

CONFIG_NAME = "build.config"


def main():
    conf = conf_init()
    print("At the end of the process a config file is generated: {}".format(CONFIG_NAME))
    print("this file is sourced at the build process! Save it, distribute it, archive it")
    print("\'{}\' is not modified in any way by the build process, just THIS tool will generate it".format(CONFIG_NAME))


def load_configuration_file(args):
    with open(args.configuration) as json_data:
        return json.load(json_data)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--configuration", help="configuration", type=str, default=None)
    parser.add_argument("-v", "--verbose", help="verbose", action='store_true', default=False)
    args = parser.parse_args()
    if not args.configuration:
        sys.stderr.write("Configuration required, please specify a valid file path, exiting now\n")
        sys.exit(EXIT_FAILURE)
    return args

def conf_init():
    args = parse_args()
    conf = load_configuration_file(args)
    return conf

if __name__ == '__main__':
    main()
