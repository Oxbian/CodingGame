import sys
import math

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = []
        self.child = []

    def addChild(self, child):
        self.child.append(child)

    def addParent(self, parent):
        self.parent.append(parent)

    def branchLength(self):
        max = 0
        for i in self.child:
            length = i.branchLength()
            if (length > max):
                max = length
        return 1 + max

nodes = []
n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    #Checking if the node is already in the tab
    existX, existY, idX, idY = 0, 0, 0, 0
    for i in range(len(nodes)):
        if nodes[i].id == x:
            existX = 1
            idX = i
        if nodes[i].id == y:
            existY = 1
            idY = i
            
    #Creating our nodes if they not exist
    if existX == 0:
        nodes.append(Node(x))
        idX = len(nodes)-1
    if existY == 0:
        nodes.append(Node(y))
        idY = len(nodes)-1

    #Adding link between nodes
    nodes[idX].addChild(nodes[idY])
    nodes[idY].addParent(nodes[idX])

max = 0
for i in range(len(nodes)):
    if nodes[i].parent == []:
        length = nodes[i].branchLength()
        if length > max:
            max = length
print(max)
