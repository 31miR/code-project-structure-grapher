import os
import fileClass

VALID_EXTENSIONS = ['c', 'h', 'cpp', 'hpp', 's', 'S']

def getFileNodesFromFolder(pathToFolder):
    result = []
    for dirPath, dirNames, dirFiles in os.walk(pathToFolder):
        for i in dirFiles:
            file = fileClass.File(dirPath, i)
            if file.getExtension() in VALID_EXTENSIONS:
                result.append(fileClass.FileNode(file, []))
    return result

def getChildNamesFromFile(file_path):
    result = []
    file = open(file_path)
    for line in file:
        if line[0:8] == "#include":
            indexStart = -1
            indexEnd = -1
            if '<' in line:
                indexStart = line.index('<') + 1
                indexEnd = line.index('>')
            elif '"' in line:
                indexStart = line.index('"') + 1
                indexEnd = indexStart + line[indexStart:].index('"')
            else:
                continue
            path = line[indexStart : indexEnd]
            path = path.split('/')
            result.append(path[-1])
    file.close()
    return result

def isNameInNodeList(name, nodeList):
    for i in nodeList:
        if name == i.file.name:
            return True
    return False

def getNodeFromNodeList(name, nodeList):
    if not isNameInNodeList(name, nodeList):
        raise Exception("There is no node with name:", name, "in a list of nodes that was given to the function")
    for i in nodeList:
        if name == i.file.name:
            return i

def setInitialChildren(nodeList):
    externals = []
    for node in nodeList:
        children = []
        childNames = getChildNamesFromFile(node.file.path+'/'+node.file.name)
        #This ugly part of code searches for external dependencies and makes nodes for them too
        externalNames = []
        for i in childNames:
            if not isNameInNodeList(i, nodeList):
                externalNames.append(i)
        for i in externalNames:
            if not isNameInNodeList(i, externals):
                externals.append(fileClass.FileNode(fileClass.File("!UNKNONWN", i), [], True))
        #End of that thing (I could've made a function just for this but I'm trying to avoid calling
        #getChildNamesFromFile again)
        for i in childNames:
            if isNameInNodeList(i, nodeList):
                children.append(getNodeFromNodeList(i, nodeList))
            else:
                children.append(getNodeFromNodeList(i, externals))
        node.children = children
    nodeList.extend(externals)
    #I realize as of writing line above that externals should have been inside nodeList
    #from the beginning and it would make this function even simpler
    #TODO, what I just said xd