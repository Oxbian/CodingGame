import sys
import math
log = lambda x: print("Debug:",x, file=sys.stderr, flush=True)
counter = 0

class Node:
    def __init__(self, char):
        self.char = char
        self.child = []
    
    def addString(self, string):
        global counter
        if (len(string) <= 0):
            return

        #log(f"Len child {len(self.child)},String = {string}")
        for i in range(len(self.child)):
            if self.child[i-1].char == string[0]:
                self.child[i-1].addString(string[1:])
                return

        newChild = Node(string[0])
        counter += 1
        self.child.append(newChild)
        self.child[len(self.child)-1].addString(string[1:])
    
head = Node("head")

n = int(input())
for i in range(n):
    telephone = input()
    head.addString(telephone)
    #log(telephone)
print(counter)
