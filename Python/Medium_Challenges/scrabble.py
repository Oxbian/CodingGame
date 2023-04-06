from collections import defaultdict

dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 
'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

n = int(input())
words = [input() for _ in range(n)]
letters = input()

#Function to check if a word is in the scrabble letters
def solve(s, t):
    freq = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
    'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for i in range(len(s)):
        freq[s[i]] += 1

    for i in range(len(t)):
        if freq[t[i]] == 0:
            return False
        freq[t[i]] -= 1
    return True

# Compare words with the given letters
max = 0
word = ""
for i in range(n):
    value = 0
    if (solve(letters, words[i]) == True):
        for j in range(len(words[i])):
            value += dict[words[i][j]]
        if value > max:
            max = value
            word = words[i]
print(word)
