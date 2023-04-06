import sys
import math

class Node:
    def __init__(self, _index, _isPasserelle, _linkedNodes):
        self.index = _index
        self.isPasserelle = _isPasserelle
        self.linkedNodes = _linkedNodes
    
    def addLink(self, newNode):
        self.linkedNodes.append(newNode)

    def removeLink (self, index):
        for i in range(len(self.linkedNodes)-1):
            if self.linkedNodes[i].index == index:
                self.linkedNodes.pop(i)

    def showInfo(self):
        print(f"Node {self.index}, est une passerelle ? {self.isPasserelle}", file=sys.stderr, flush=True)

    def showFull(self):
        print(f"\nInformation du noeud:\nNode {self.index}, est une passerelle ? {self.isPasserelle}", file=sys.stderr, flush=True)
        for node in self.linkedNodes:
            node.showInfo()

def foundClosestPass(nodeList, passId, si):
    for i in passId:
        for j in range(len(nodeList[i].linkedNodes)):
            if nodeList[i].linkedNodes[j].index == si:
                return i
    return 0

def foundNodeToCut(nodeList, si):
    passerelle = foundClosestPass(nodeList, passId, si)
    #nodeList[passerelle].showFull()
    for i in range(len(nodeList[passerelle].linkedNodes)):
        if nodeList[passerelle].linkedNodes[i].index == si:
            print(nodeList[passerelle].index, nodeList[si].index)
            return
    print(nodeList[passerelle].index, nodeList[passerelle].linkedNodes[0].index)

nodeList = []
passId = 0
n, l, e = [int(i) for i in input().split()]
for i in range(n):
    nodeList.append(Node(i, False, [])) #Initialisation des noeuds

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    nodeList[n1].addLink(nodeList[n2])
    nodeList[n2].addLink(nodeList[n1])

passId = [int(input()) for i in range(e)]
for i in passId:
    nodeList[i].isPasserelle = True

for node in nodeList:
    node.showFull()


# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    print(si, file = sys.stderr, flush = True)
    foundNodeToCut(nodeList ,si)