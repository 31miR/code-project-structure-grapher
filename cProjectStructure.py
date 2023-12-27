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

