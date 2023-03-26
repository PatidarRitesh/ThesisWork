# use xmltree to read an xml file
import xml.etree.ElementTree as ET
import re
tree = ET.parse('output.xml')
root = tree.getroot()
TITLE_output = ''


for child in root:
    if re.search('title', child.tag):
        TITLE_output = child.text
    if re.search('creator', child.tag):
        for personname in child:
            if re.search('personname', personname.tag):
                for data in personname:
                    print(data.text)
        # print(child.find('*').text)
        # get entire data from creator

        

