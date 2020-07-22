#! /usr/bin/env python

import sys

if len(sys.argv) != 2:
    print("#usage: python {sys.argv[0]} [txt]")
    sys.exit()

f = sys.argv[1]

try:
with open(f, 'r') as handle:
     read = handle.readlines()


except FileNotFoundError:
    print(f"{f} not found.. please chck..")
    sys.exit()

print(read)

