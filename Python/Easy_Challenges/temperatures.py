import sys
import math

n = int(input())  # the number of temperatures to analyse
min = float('inf')
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if (abs(0-t) < abs(0-min)):
        min = t
    elif min == t:
        min = t
    elif abs(min) == abs(t):
        min = abs(min)

if (min == float('inf')):
    print(0)
else:
    print(min)
