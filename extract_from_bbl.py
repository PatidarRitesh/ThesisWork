# import xml.etree.ElementTree as ET

# # read in the bbl file data
# with open('input.bbl', 'r') as f:
#     bbl_data = f.read()

# # split the bbl data into individual entries
# entries = bbl_data.split('\\bibitem')

# # create the root element for the XML document
# root = ET.Element('bibliography')

# # iterate over the entries and add them to the XML document
# for entry in entries[1:]:
#     # split the entry into individual lines
#     lines = entry.strip().split('\n')
#     # get the label (first line of the entry)
#     label = lines[0].strip()
#     # create the entry element
#     entry_elem = ET.SubElement(root, 'entry', {'label': label})
#     # iterate over the remaining lines and create elements for each field
#     print(lines)
#     for line in lines[1:]:
#         parts = line.split('=')
#         key = parts[0].strip()[1:-1]
#         value = parts[1].strip()[1:-1]  # remove the extra -2 slice
#         field_elem = ET.SubElement(entry_elem, key)
#         field_elem.text = value

# # write the XML document to a file
# tree = ET.ElementTree(root)
# tree.write('output_bbl.xml', encoding='utf-8', xml_declaration=True)



import xml.etree.ElementTree as ET

def fetch_author_names(fields):
    author = fields[1].strip()
    author = author[1:-1]
    author_elem = ET.SubElement(entry_elem, 'author')
    author_elem.text = author
    print('author')


with open('input.bbl', 'r') as f:
    bbl_data = f.read()

# split the bbl data into entries
entries = bbl_data.split('\\bibitem')

# create the root element for the XML document
root = ET.Element('bibliography')

# iterate over the entries and add them to the XML document
for entry in entries[1:]:  # ignore the first empty entry
    # split the entry into fields
    fields = entry.split('\n')
    label = fields[0].strip()

    # create the entry element
    entry_elem = ET.SubElement(root, 'entry', {'label': label})

    # iterate over the fields and add them to the entry element
    for field in fields:
        print(field)

    fetch_author_names(fields)
    fetch_year(fields)
    fetch_title(fields)
    fetch_journal(fields)
    fetch_volume(fields)
    fetch_number(fields) # optional
    fetch_pagesfields(fields)
    fetch_doi(fields) # optional
    fetch_url(fields) # optional


    # for field in fields[1:]:
    #     field = field.strip()
    #     if not field:
    #         continue
    #     key, value = field.split(',', 1)
    #     key = key.strip()
    #     value = value.strip()[1:-1]
    #     field_elem = ET.SubElement(entry_elem, key)
    #     field_elem.text = value

# write the XML document to a file
tree = ET.ElementTree(root)
tree.write('output_bbl.xml', encoding='utf-8', xml_declaration=True)
