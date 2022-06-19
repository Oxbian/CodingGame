import sys

x_min = 2**30
x_max = -2**30

y_list = []
nb_buildings = int(input())
for i in range(nb_buildings):
    x, y = map(int, input().split())
    y_list.append(y)
    print(x,y, file=sys.stderr, flush=True)
    if (x > x_max) : x_max = x
    if (x < x_min) : x_min = x

cable_length = x_max - x_min
y_list.sort()
y_median : int = y_list[nb_buildings // 2]

for y in y_list:
    cable_length += abs(y_median - y)

print(cable_length)
