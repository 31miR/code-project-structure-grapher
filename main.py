import cProjectStructure
import graphics

#main guard in case this program is also [for some weird reason] used as a library
def main():
    print("Please provide a relative path to the folder you want to analyze")
    print("You can use . and .. in the path string")
    rel_path = str(input('path:'))
    nodes = cProjectStructure.getFileNodesFromFolder(rel_path)
    cProjectStructure.setInitialChildren(nodes)
    graphics.drawNodeList(nodes)
    graphics.produce("nodes.html")
    return 0

if __name__ == '__main__':
    main()