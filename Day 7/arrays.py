#!/bin/python
from __future__ import print_function
import sys


n = int(raw_input().strip())
arr = list(map(int,raw_input().strip().split(' ')))
arr.reverse()

print(*arr,sep=' ')