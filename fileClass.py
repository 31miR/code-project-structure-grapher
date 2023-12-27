class File:
    def __init__(self, path, name):
        self.path = path
        self.name = name
    def getExtension(self):
        parts = self.name.split('.')
        if (len(parts) < 2):
            return "NO EXTENSION"
        return parts[-1]
    def __str__(self):
        return self.name

class FileNode:
    def __init__(self, currentFile, children, isExternal = False):
        self.file = currentFile
        self.children = children
        self.isExternal = isExternal
    def __str__(self):
        return "{node name: " + self.file.name + " with children: " + str([i.file.name for i in self.children]) + "}"