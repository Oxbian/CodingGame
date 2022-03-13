import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    d[ext.lower()] = mt

for i in range(q):
    fname = input().lower().split(".")  # One file name per line.
    #print(stderr,fname)
    if (len(fname) == 2 and fname[1] in d):
        print(d[fname[1]])
    elif (len(fname) > 2 and fname[len(fname)-1] in d):
        print(d[fname[len(fname)-1]])
    else:
        print("UNKNOWN")
    