import sys
import math

n = int(input())
pi = [int(input()) for i in range(n)]
pi.sort()
min = float('inf')
for i in range(1,n):
    if (pi[i] - pi[i-1] < min):
        min = pi[i] - pi[i-1]

print(min)
