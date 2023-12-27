class File:
    def __init__(self, path, name):
        self.path = path
        self.name = name
    def getExtension(self):
        parts = self.name.split('.')
        if (len(parts) < 2):
            return "NO EXTENSION"
        return parts[-1]