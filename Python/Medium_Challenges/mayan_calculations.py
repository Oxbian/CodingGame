import sys

#Function to split a string into a list of n char strings
def split(string, size):
    i=0
    liste=[]
    while(i<len(string)):
        liste.append(string[i:i+size])
        i+=size
    return(liste)

patterns = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [],
    12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: []}

num_1line, num_2line = [], []
separator = "\n"

l, h = [int(i) for i in input().split()]
splitted = []
for i in range(h):
    numeral = input()
    splitted.append(split(numeral, l))
print(f"splitted {splitted}", file=sys.stderr, flush = True)

# Adding numbers patterns
for i in range(h):
    for j in range (20):
        patterns[j].append(splitted[i][j])
print(patterns, file= sys.stderr, flush=True)

# Getting all the line of the first number
s1 = int(input())
for i in range(s1):
    num_1line.append(input())

# Getting all the line of the second number
s2 = int(input())
for i in range(s2):
    num_2line.append(input())

operation = input()

n1, n2 = 0, 0

while (len(num_1line) != 0 or len(num_2line) != 0):
    for i in range (20):
        if separator.join(num_1line[:h]) == separator.join(patterns[i]):
            n1 += i * 20**(len(num_1line) // h -1)
            num_1line = num_1line[h:]

        if separator.join(num_2line[:h]) == separator.join(patterns[i]):
            n2 += i * 20**(len(num_2line) // h -1)
            num_2line = num_2line[h:]

    print(f"{n1} {operation} {n2}", file=sys.stderr, flush=True)

result = 0
if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2    
elif operation == "/":
    result = n1 / n2

#Identify the maximum power we need
power = 0
while (20**power < result):
    power+= 1

# Loop printing the numbers we need
for i in range(1,power):
    quotient = result // (20**(power-i))
    print(f"Debug: resultat {result}, puissance {20**(power-1)}, quotient {quotient}", file=sys.stderr, flush = True)
    print(separator.join(patterns[quotient]))
    result -= 20**(power-i) * quotient
    print(f"Debug: reste {result}", file=sys.stderr, flush=True)

# Printing the rest under 20^1
print(separator.join(patterns[result]))