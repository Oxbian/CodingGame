import sys
log = lambda x : print(x, file=sys.stderr, flush = True)

n = int(input())
gift = int(input())
money = sorted(int(input()) for _ in range(n))

if (sum(money) < gift): #If the pilipius hasn't enough money for the gift
    print("IMPOSSIBLE")
else: #else count the part of each
    for i in range(n-1):
        #log(f"Prix restant: {gift}, n {n-i}, {gift // (n-i)}")
        if  money[i] > (gift // (n-i)):
            print(gift//(n-i))
            gift -= gift // (n-i)
        else:
            print(money[i])
            gift -= money[i]
    print(gift)