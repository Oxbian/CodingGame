import sys

r = int(input()) #Number of the origin
l = int(input()) #Line we want to found
#print(r,l, file=sys.stderr, flush=True)

def conway(n,tour):
    if (tour == l-1):
        print(n)
        return

    tab = n.split()
    n = ""
    number = tab[0]
    occurrency = 1

    for i in range(1, len(tab)):
        if (number == tab[i]):
            occurrency += 1
        elif (number != " "):
            if (len(n) > 1):
                n += " " + str(occurrency) +" " + str(number)
            else:
                n += str(occurrency) +" " + str(number)
            number = tab[i]
            occurrency = 1
    if (len(n) > 1):
        n += " " + str(occurrency) +" " + str(number)
    else:
        n += str(occurrency) + " " + str(number)
    conway(n, tour+1)

conway(str(r),0)
