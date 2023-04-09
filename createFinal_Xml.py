import xml.etree.ElementTree as ET

# Open the first XML file and parse it
xml_file_1 = 'output.xml'
tree_1 = ET.parse(xml_file_1)
root_1 = tree_1.getroot()

def tag_uri_and_name(elem):
    if elem.tag[0] == "{":
        uri, ignore, tag = elem.tag[1:].partition("}")
    else:
        uri = None
        tag = elem.tag
    return uri, tag

uri, tag = tag_uri_and_name(root_1)

print(uri, tag)


# Find the specific tag you want to append to
tag = root_1.findall('{'+uri+'}bibliography')
# print(tag)
# Open the second XML file and parse it
xml_file_2 = 'output_bbl.xml'
tree_2 = ET.parse(xml_file_2)
root_2 = tree_2.getroot()

# add all the childern of root_2 to root_1 where the tag is bibliography
root_1.findall('{'+uri+'}bibliography').extend(root_2)

# tag_s = root_1.findall('{'+uri+'}bibliography')

# print("TAG_S",tag_s[0])
# print([child for child in tag_s[0]])

# print([child for child in root_2])
# Append the elements from the second XML file to the specific tag in the first XML file
entries = [child for child in root_2]
for entry in entries:
    tag[0].append(entry)

print(tag[0])
print([child for child in tag[0]])
# print(root_2.tag)
# tag.extend(root_2)

# print(tag)

# Write the modified XML to a new file
new_xml_file = 'output_final.xml'
tree_1.write(new_xml_file, encoding='utf-8', xml_declaration=True)


# import xml.etree.ElementTree as ET

# # Open the first XML file and parse it
# xml_file_1 = 'output.xml'
# tree_1 = ET.parse(xml_file_1)
# root_1 = tree_1.getroot()

# # Open the second XML file and parse it
# xml_file_2 = 'output_bbl.xml'
# tree_2 = ET.parse(xml_file_2)
# root_2 = tree_2.getroot()

# # Create a new root element
# new_root = ET.Element('new_root')

# # Append the root elements of the original files as child elements of the new root
# new_root.append(root_1)
# new_root.append(root_2)

# # Create a new XML tree with the new root
# new_tree = ET.ElementTree(new_root)

# # Write the new XML to a file
# new_xml_file = 'output_final.xml'
# new_tree.write(new_xml_file, encoding='utf-8', xml_declaration=True)
