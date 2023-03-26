# import xml.etree.ElementTree as ET

# # Define the XML file path
# xml_file = 'output.xml'

# # Parse the XML file using ElementTree
# tree = ET.parse(xml_file)
# root = tree.getroot()

# # Extract the paper title
# title_elem = root.find('.//{http://purl.org/dc/elements/1.1/}title')
# if title_elem is not None:
#     title = title_elem.text
# else:
#     title = None

# # Extract author information
# authors = []
# for author_elem in root.findall('.//{http://www.tei-c.org/ns/1.0}author'):
#     # Extract the author name
#     name_elem = author_elem.find('{http://www.tei-c.org/ns/1.0}persName')
#     firstname_elem = name_elem.find('{http://www.tei-c.org/ns/1.0}forename')
#     if firstname_elem is not None:
#         firstname = firstname_elem.text
#     else:
#         firstname = None
#     lastname_elem = name_elem.find('{http://www.tei-c.org/ns/1.0}surname')
#     if lastname_elem is not None:
#         lastname = lastname_elem.text
#     else:
#         lastname = None
#     if firstname is not None and lastname is not None:
#         name = f'{firstname} {lastname}'
#     else:
#         name = None

#     # Extract the author email
#     email_elem = author_elem.find('{http://www.tei-c.org/ns/1.0}email')
#     if email_elem is not None:
#         email = email_elem.text
#     else:
#         email = None
    
#     # Extract the author affiliation
#     affiliation_elem = author_elem.find('{http://www.tei-c.org/ns/1.0}affiliation')
#     if affiliation_elem is not None:
#         affiliation = affiliation_elem.text
#     else:
#         affiliation = None
    
#     author_info = {'name': name, 'email': email, 'affiliation': affiliation}
#     authors.append(author_info)

# # Print the extracted information
# print(f'Title: {title}')
# print('Authors:')
# for author in authors:
#     if author['name'] is not None:
#         print(f'- Name: {author["name"]}')
#     if author["email"] is not None:
#         print(f'  Email: {author["email"]}')
#     if author["affiliation"] is not None:
#         print(f'  Affiliation: {author["affiliation"]}')



import re

# Define the XML file path
xml_file = 'output.xml'

# Load the XML file into a string
with open(xml_file, 'r') as f:
    xml_str = f.read()

# Define the regular expression patterns to match the paper title, authors, emails, and affiliations
title_pattern = r'(?:<title.*?>)(.*?)(?:<\\/title>)'
author_pattern = r'<tei:author.*?>\s*<tei:persName.*?><tei:forename.*?>(.*?)<\/tei:forename>\s*<tei:surname.*?>(.*?)<\/tei:surname><\/tei:persName>\s*(<tei:email.*?>.*?<\/tei:email>)?\s*(<tei:affiliation.*?>.*?<\/tei:affiliation>)?\s*<\/tei:author>'

# Extract the paper title using regular expressions
match = re.search(title_pattern, xml_str)
if match is not None:
    title = match.group(1)
else:
    title = None

# Extract author information using regular expressions
authors = []
for match in re.finditer(author_pattern, xml_str):
    firstname = match.group(1)
    lastname = match.group(2)
    email = match.group(3)
    affiliation = match.group(4)
    author_info = {'name': f'{firstname} {lastname}', 'email': email, 'affiliation': affiliation}
    authors.append(author_info)

# Print the extracted information
print(f'Title: {title}')
print('Authors:')
for author in authors:
    print(f'- Name: {author["name"]}')
    if author["email"] is not None:
        print(f'  Email: {author["email"]}')
    if author["affiliation"] is not None:
        print(f'  Affiliation: {author["affiliation"]}')
