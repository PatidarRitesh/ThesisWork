# use xmltree to read an xml file
import xml.etree.ElementTree as ET
import re
tree = ET.parse('output.xml')
root = tree.getroot()
TITLE_output = ''

namespace = root.tag.split('}')[0].strip('{')
print(namespace)

for child in root:
    if re.search('title', child.tag):
        TITLE_output = child.text
        print("Title: ",TITLE_output)
        print("=====================================")
    if re.match("{" + namespace + "}creator", child.tag):
    # if re.search('creator', child.tag):
        for personname in child:
            if re.match("{" + namespace + "}personname", personname.tag):
            # if re.search('personname', personname.tag):
                # print(personname.text)
                for c in personname.itertext():
                    if re.search('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', c):
                        print(c)
                        print("=====================================")
                    else:
                        print(c)
                    # if c.text != None:
                    #     if re.search('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', c.text):
                    #         print(c.text)
                    #         print("=====================================")  
                    # else:   
                    #     if c.tail:                   
                    #         print(c.tail)

for child in root:
    if re.match("{" + namespace + "}section", child.tag):
        for key in child.attrib:
            if re.match('^{[^{}]*}id', key):
                print("ID:",child.attrib[key])
        for subchild in child.iter():
            if subchild.tag == "{" + namespace + "}title":
                for c in subchild.itertext():
                    print(c)


        

