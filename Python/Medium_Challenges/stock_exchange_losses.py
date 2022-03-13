n = int(input())
max = 0
max_lost = 0
for i in input().split():
    curr_lost = int(i) - max
    if (curr_lost < max_lost):
        max_lost = curr_lost
    if (int(i) > max):
        max = int(i)
print(max_lost)