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
import re

def fetch_author_names(fields):
    # fields = fields.split('\n')
    # author_list = fields[1].strip().split('.')[0]
    # author_list = author_list.split(',')
    # author_list_1 = [author.strip().strip('and').strip() for author in author_list]

    # # input(author_list_1)
    # # enumerate(author_list_1)
    # author_elem_list = []
    # for i, author in enumerate(author_list_1):
    #     author_elem = ET.SubElement(entry_elem, f'author{i}')
    #     author_elem_list.append(author_elem)
    #     author_elem.text = author
    #     print(f'author{i+1}: {author}')
    return fields

def fetch_year(fields):
    return int(fields)
    # fields = fields.split('\n')
    # year = fields[1].strip().split('.')[1].strip()
    # year_elem = ET.SubElement(entry_elem, 'year')
    # year_elem.text = year
    # print(f'year: {year}')

def fetch_id(data):
    return data


def fetch_title(fields):
    fields =[field.strip() for field in fields.split('\n')]
    title = " ".join(fields)
    title_elem = ET.SubElement(entry_elem, 'title')
    title_elem.text = title
    print(f'title: {title}')
    

def fetch_journal(fields):
    # fields = fields.split('{')[1].split('}')[0]
    # fields = [field.strip() for field in fields.split('\n')]
    # journal = " ".join(fields).split('(')[0]
    # journal_elem = ET.SubElement(entry_elem, 'journal')
    # journal_elem.text = journal
    # print(f'journal: {journal}')
    return fields.strip()

def fetch_volume(fields):
    if 'Volume' not in fields:
        return None
    fields = fields.split('{')[1].split('}')[0]
    fields = [field.strip() for field in fields.split('\n')]
    volume = " ".join(fields).split('(')[1].split(":")[1].strip(')')
    volume_elem = ET.SubElement(entry_elem, 'volume')
    volume_elem.text = volume
    print(f'volume: {volume}')

# def fetch_number(fields):
#     number = fields[6].strip()
#     number = number[1:-1]
#     number_elem = ET.SubElement(entry_elem, 'number')
#     number_elem.text = number
#     print('number')
#     print(number)

def fetch_pages(fields):
    page_range = fields.strip('.').split("--")
    
    pages_elem_start = ET.SubElement(entry_elem, 'pages_start')
    pages_elem_end = ET.SubElement(entry_elem, 'pages_end')
    pages_elem_start.text = page_range[0].strip()
    pages_elem_end.text = page_range[1].strip()
    print(f'Pages from {page_range[0]} to {page_range[1]}')

# def fetch_doi(fields):
#     doi = fields[8].strip()
#     doi = doi[1:-1]
#     doi_elem = ET.SubElement(entry_elem, 'doi')
#     doi_elem.text = doi
#     print('doi')
#     print(doi)

def fetch_url(fields):
    # to be done with regexp
    return None

# read in the bbl file data
with open('input.bbl', 'r') as f:
    bbl_data = f.read()

# split the bbl data into entries
entries = bbl_data.split('\\bibitem')

# create the root element for the XML document
root = ET.Element('bibliography')

# iterate over the entries and add them to the XML document
for entry in entries[1:]:  # ignore the first empty entry
    print("====================================")
    # split the entry into fields
    fields = entry.split('\\newblock')
    label = fields[0].strip()
    
    # create the entry element
    entry_elem = ET.SubElement(root, 'entry', {'label': label})

    # # iterate over the fields and add them to the entry element
    # for field in fields:
    #     print(field)
    try:
        # pattern_1 = r'\[\{(.+)(\(\d\d\d\d\))([A-Za-z\s,]*)\}\]\{([A-Za-z0-9:_-]+)\}[\r\s]*([A-Za-z0-9\s,.~]+)([\d]{4})'
        # pattern_1 = r'\[\{(.+)(\(\d\d\d\d\))([A-Za-z\s,]*)\}\]\{([A-Za-z0-9:_-]+)\}[\r\s]*(.+)([\d]{4})'
        pattern_1 = r'\[\{(.+)(\(\d\d\d\d\))(.*)\}\]\{([A-Za-z0-9:_-]+)\}[\r\s]*(.+)([\d]{4})'
        pattern_3 = r'.*\{([A-Za-z0-9\s\r.,:()]+)(\(.*:(.*)\))?\}(,\s*(pages\s*|[\d]+:)([\d-]+)|.)'

        # process the fields string by removing newlines and spaces
        
        fields[0] = fields[0].strip().replace('\n', ' ')
        data_1 = re.sub('\s+',' ',fields[0])
        matched_data = re.findall(pattern_1, data_1)[0]

        fields[2] = fields[2].strip().replace('\n', ' ')
        data_3 = re.sub('\s+',' ',fields[2])
        # print(data_3)
        matched_data_3 = re.findall(pattern_3, data_3)[0]
        # print(matched_data_3)
        # input()
        try:
            print(f'Authors: {fetch_author_names(matched_data[4])}')
        # print whatever type of error in except block
        except Exception as e:
            print(e)
        
        try:
            print(f'Year: {fetch_year(matched_data[5])}')
        except Exception as e:
            print(e)

        try:
            print(f'ID: {fetch_id(matched_data[3])}')
        except Exception as e:
            print(e)

        try: 
            fetch_title(fields[1])
        except Exception as e:
            print(e)

        try:
            print(f'Journal: {fetch_journal(matched_data_3[0])}')
        except Exception as e:
            print(e)

        try:
            fetch_volume(fields[2])
        except Exception as e:
            print(e)

        try:
            fetch_pages(matched_data_3[5])
        except Exception as e:
            # print(e)
            print("No pages found")
        # try:    
        #     fetch_doi(fields) # optional
        # except Exception as e:
        #     print(e)

        try:   
            fetch_url(fields[1]) # optional
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)





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
