import xml.etree.ElementTree as ET

def read(file)
    tree = ET.parse(file)
    return tree.getroot

def write(fileName, fileContent):
    file = open(fileName, 'w')    
    file.write(fileContent)
    file.close()