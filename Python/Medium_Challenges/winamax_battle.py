import sys
import math

val = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

n = int(input())  # the number of cards for player 1
cardp_1 = [val[input()[:-1]] for i in range(n)]
m = int(input())  # the number of cards for player 2
cardp_2 = [val[input()[:-1]] for i in range(m)]

round = 0

def smallest_deck(): return min(len(cardp_1), len(cardp_2))

while ( smallest_deck() > 0):
    round+=1
    print(cardp_1, cardp_2, file=sys.stderr, flush=True)
    compare = 0
    while (cardp_1[compare] == cardp_2[compare]):
        compare += 4
        if compare > smallest_deck(): print("PAT"); break

    if cardp_1[compare] > cardp_2[compare]:
        cardp_1 = cardp_1[compare+1:] + cardp_1[:compare+1] + cardp_2[:compare+1]
        cardp_2 = cardp_2[compare+1:]
    else:
        cardp_2 = cardp_2[compare+1:] + cardp_1[:compare+1] + cardp_2[:compare+1]
        cardp_1 = cardp_1[compare+1:]

winner = 1 if len(cardp_2) == 0 else 2
    
print(winner, round)