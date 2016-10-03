#!/bin/python

import sys

n = int(raw_input().strip())

binary = list(bin(n)[2:])
#print (binary)

count = 0
max_count = 0
for i in binary:
    if (i == '1'):
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print (max_count)