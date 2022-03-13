import sys
import math

def distance (latA, lonA, latB, lonB):
    x = (float(lonB) - float(lonA)) * math.cos((float(latA) + float(latB)) / 2)
    y = (float(latB) - float(latA))
    return math.sqrt(x**2 + y**2) * 6371

lon = input()
lon = float(lon.replace(",", "."))
lat = input()
lat = float(lat.replace(",", "."))
n = int(input())
defib = [input() for i in range(n)]
minDist = float('inf')
minName = ""

for i in range(n):
    entry = defib[i].split(';')
    dist = distance(lat, lon, float(entry[5].replace(",", ".")), float(entry[4].replace(",", ".")))
    if (dist < minDist):
        minDist = dist
        minName = entry[1]

print(minName)
