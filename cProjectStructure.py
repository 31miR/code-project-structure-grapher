import os
import fileClass

VALID_EXTENSIONS = ['.c', '.h', '.cpp', '.hpp', '.s', '.S']

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