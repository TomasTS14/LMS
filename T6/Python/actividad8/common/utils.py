import xml.etree.ElementTree as ET


def read(file):
    tree = ET.parse(file)
    return tree.getroot()


def write(fileName, content):
    file = open(fileName, 'w')
    file.write(content)
    file.close()
