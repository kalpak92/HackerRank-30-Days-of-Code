#!/bin/python

import sys

n = int(raw_input().strip())

for i in range(1, 11):
    a = str(n) + ' x ' + str(i) + ' = ' + str(n*i)
    sys.stdout.write (a + '\n')