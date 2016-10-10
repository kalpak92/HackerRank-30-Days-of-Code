#!/bin/python

import sys


S = raw_input().strip()

try:
    n = int(S)
    print(n)
except:
    print("Bad String")