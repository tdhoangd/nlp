from lxml import etree as et
import gzip
import sys

if len(sys.argv) < 2:
    raise Exception('Missing files path from command line arguments')

files = sys.argv[1:]

for xmlGz in files:
    f = gzip.open(xmlGz, 'rb')
    tree = et.parse(f)
    f.close()

    root = tree.getroot()
    for document in root.getchildren():
        
        if (document.attrib['type'] != 'story'):
            continue
        
        text = None
        for isText in document.getchildren():
            if isText.tag == 'TEXT':
                text = isText

        if (text != None):    
            paragraphs = text.getchildren()
            for paragraph in paragraphs:
                if (paragraph.tag == 'P'):
                    print (paragraph.text)
 