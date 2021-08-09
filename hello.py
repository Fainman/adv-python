#!/usr/bin/env python3
# Purpose: Say Hello to Waldo

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')

# print("Hello Waldo")

