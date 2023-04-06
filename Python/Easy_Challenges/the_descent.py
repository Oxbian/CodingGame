import sys
import math

# game loop
while True:
    mountain_h = [int(input()) for i in range(8)]  # represents the height of one mountain.
    print(mountain_h.index(max(mountain_h)))
