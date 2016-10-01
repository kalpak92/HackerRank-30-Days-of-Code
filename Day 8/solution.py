from __future__ import print_function
n = int(raw_input())

d = {}

for i in xrange(n):
    name, number = raw_input().split()
    
    d[name]=number

while(True):
    try:
        name = raw_input()
    except EOFError:
        break
    
    if name in d:
        print ("{}={}".format(name,d[name]))
    else:
        print("Not found")
