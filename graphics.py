import pyvis
import fileClass

NETWORK = pyvis.network.Network(layout=True, directed=True)

#function expects that the node children are already drawn
def drawNode(node):
    NETWORK.add_node(node.file.name)
    for i in node.children:
        NETWORK.add_edge(node.file.name, i.file.name)

def isDrawingPossible(node, alreadyDrawn):
    names = [i.file.name for i in alreadyDrawn]
    if node in alreadyDrawn:
        return False
    for i in node.children:
        if i.file.name not in names:
            return False
    return True

#This is assuming that each branch has an end, that is there is no weird looping in the tree
#Which is a healthy assumption if the project is properly written
def drawNodeList(nodeList):
    drawn = []
    level = 0
    while(len(drawn) != len(nodeList)):
        for i in nodeList:
            if isDrawingPossible(i, drawn):
                drawNode(i)
                drawn.append(i)
        level += 1

def produce(fileName, allow_options = False):
    if allow_options:
        NETWORK.show_buttons()
    NETWORK.hrepulsion()
    NETWORK.toggle_physics(False)
    NETWORK.show(fileName, notebook=False)