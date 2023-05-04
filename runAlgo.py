import os
import xml.etree.ElementTree as ET
import re


def init_dict():

    information = {
        'title': '',
        'book': '',
        'publisher': '',
        'Pages': '',
        'year': '',
        'ID': '',
        'volume': '',
        'author': list()
    }
    return information

def get_information(Matched_data,information, paper_format="ACL/M"):
    
    if paper_format == 'ACL/M':
        print(Matched_data['1'])
        information['author'] = list()
        if len(Matched_data['1']):
            for tup in Matched_data['1']:
                if tup[0] == '':
                    information['author'].append(tup[1])
                else:
                    information['author'].append(tup[0])

        if len(Matched_data['2']):
            information['year'] = Matched_data['2'][0]
        
        elif len(Matched_data['10']):
            information['year'] = Matched_data['10'][0]

        if len(Matched_data['3']):
            information['ID'] = Matched_data['3'][0]

        if len(Matched_data['4']):
            if len(Matched_data['4'][0]):
                information['title'] = Matched_data['4'][0]
            else:
                information['title'] = Matched_data['4']

        if len(Matched_data['5']):
            information['book'] = Matched_data['5'][0]
        
        if len(Matched_data['6']):
            information['publisher'] = Matched_data['6'][0]

        else:
            if len(Matched_data['9']):
                if Matched_data['9'][0][0] == '':
                    information['publisher'] = information.get('publisher', '') +  f"Journal: {Matched_data['9'][0][1]}"
                else:
                    information['publisher'] = information.get('publisher', '') +  f"Journal: {Matched_data['9'][0][0]}"

        if len(Matched_data['11']):
            information['volume'] = Matched_data['11'][0]
        
        if len(Matched_data['12']):
            information['Pages'] = Matched_data['12'][0]

        elif len(Matched_data['7']):
            information['Pages'] = Matched_data['7'][0]

    return information



directory = './'

for filename in os.listdir(directory):
    if filename.endswith('.bbl'): # if you only want to read bbl files
        with open(os.path.join(directory, filename), 'r') as file:
            bbl_data= file.read()
            #print(content)
            # process the contents of the file here
            print("====================================")
            print("current file:")
            print(filename)







            
        

    
        
        

            # paper_name = input("Enter the name of the paper: ")
            # # read in the bbl file data
            # with open(f'{paper_name}.bbl', 'r', encoding="utf8") as f:
            #     bbl_data = f.read()

            # split the bbl data into entries
            entries = bbl_data.split('\\bibitem')

            # create the root element for the XML document
            root = ET.Element('bibliography')

            for entry in entries[1:]:  # ignore the first empty entry

                # split the entry into fields
                print(entry)
                print("====================================")
            
                
                fields = entry.split('\\newblock')
                # print(fields[0])

                label = fields[0].strip()
                # print(label)
                
                # create the entry element
                entry_elem = ET.SubElement(root, 'entry', {'label': label})


                file_type = 'ACL/ACM'
                # process the fields string by removing newlines and spaces
                
                fields[0] = fields[0].strip().replace('\n', ' ')
                fields[2] = fields[2].strip().replace('\n', ' ')
                fields[1] = fields[1].strip().replace('\n', ' ')
                data_1 = re.sub('\s+',' ',fields[0])
                data_2 = re.sub('\s+',' ',fields[1])
                data_3 = re.sub('\s+',' ',fields[2])

                print("AUTHORS: ", data_1)
                print("TITLE: ", data_2)
                print("PUBLICATION: ", data_3)
                print("====================================")

                Patterns = { 
                    'Author_ACM_ACL_1' : r'''{person}{([A-Za-z0-9\s~.]+)({[\\'\w\d\s"-]+}[\d\w\s-]*)*''',
                    'YEAR_ACM_ACL_1' : r'''{year}{(\d{4})}''',
                    'BIB_ACM_ACL_1' : r'''\]% {([\w\d\s:\/-]+)}''',
                    'Article_ACM_ACL_2' : r'''\\showarticletitle{([\w\d\s:{}“”;_$%*@!,.?-]*)}''',
                    'Book_ACM_ACL_2' : r'''booktitle}{\\emph{([\w\s:,{}*;"'()\/-]+)}}''',
                    'Publisher_ACM_ACL_2' : r'''bibinfo{publisher}{{?([\w\s]+)''',
                    'Page_ACM_ACL_2' : r'''bibinfo{pages}{(\d+)(-+)?(\d*)''',
                    'Title_IEEE_ARXIV_CVPR_2' : r'''((\bhttps:.+)}\s{)?|([\w\s,'":\/—-]*)'''   ,

                    'Journal_ACM_3' : r'''journal}{\\emph{([\w\s.]+)|url{([^}]*)}''',

                    'Year_ACM_ACL_3' : r'''bibinfo{year}{(\d{4})''',
                    'Volumne_ACM_ACL_3' : r'''bibinfo{volume}{(\d+)''',
                    'Pages_ACM_ACL_3' : r'''bibinfo{pages}{(\d+)(-+)?(\d*)''',
                    'Pages_IEEE_ARXIV_CVPR_3' : r'''(\d+)-+(\d+)''',

                    'Publisher_IEEE_aRXIV_CVPR_3' : r'''em[ph{\s]+([^}]+)'''

                }

                Matched_data = dict()
                # print("---------------- DATA 1 --------------------")

                Matched_data['1'] = re.findall(Patterns["Author_ACM_ACL_1"], data_1)
                # print(" ACL/M AUTHORS: ", end=" ")
                # print(Matched_data["1"]) if len(Matched_data["1"]) else print(F"No match: {data_1}")

                Matched_data['2'] = re.findall(Patterns["YEAR_ACM_ACL_1"], data_1)
                # print("ACL/M YEAR: ", end=" ")
                # print(Matched_data['2']) if len(Matched_data['2']) else print("No match")

                Matched_data['3'] = re.findall(Patterns["BIB_ACM_ACL_1"], data_1)
                # print("ACL/M BIB: ", end=" ")
                # print(Matched_data['3']) if len(Matched_data['3']) else print("No match")

                # print("---------------- DATA 2 --------------------")

                

                Matched_data['4'] = re.findall(Patterns["Article_ACM_ACL_2"], data_2)
                # print("ACL/M Article TItle: ", end= " ")
                # print(Matched_data['4']) if len(Matched_data['4']) else print(f"No match ")
                Matched_data['5'] = re.findall(Patterns["Book_ACM_ACL_2"], data_2)
                # print("ACL/M Book Title: ", end=" ")
                # print(Matched_data['5']) if len(Matched_data['5']) else print("No match")

                Matched_data['6'] = re.findall(Patterns["Publisher_ACM_ACL_2"], data_2)
                # print("ACM/L Publisher: ", end=" ")
                # print(Matched_data['6']) if len(Matched_data['6']) else print("No match")

                Matched_data['7'] = re.findall(Patterns["Page_ACM_ACL_2"], data_2)
                # print("ACL/M Pages: ", end=" ")
                # print(Matched_data['7']) if len(Matched_data['7']) else print("No match")

                Matched_data['8'] = re.findall(Patterns["Title_IEEE_ARXIV_CVPR_2"], data_2)
                # print("IEEE Title: ", end=" ")
                # print(Matched_data['8']) if len(Matched_data['8']) else print(f"No match")

                # print("-------------- DATA 3 ------------------")

                Matched_data['9'] = re.findall(Patterns["Journal_ACM_3"], data_3)
                # print("ACL/M Journal: ", end=" ")
                # print(Matched_data['9']) if len(Matched_data['9']) else print("No match")

                Matched_data['10'] = re.findall(Patterns["Year_ACM_ACL_3"], data_3)
                # print("ACl/M Year: ", end=" ")
                # print(Matched_data['10']) if len(Matched_data['10']) else print("No match")

                Matched_data['11'] = re.findall(Patterns["Volumne_ACM_ACL_3"], data_3)
                # print("ACL/M Volumne: ", end=" ")
                # print(Matched_data['11']) if len(Matched_data['11']) else print("No match")

                Matched_data['12'] = re.findall(Patterns["Pages_ACM_ACL_3"], data_3)
                # print("ACL/M Pages: ", end=" ")
                # print(Matched_data['12']) if len(Matched_data['12']) else print("No match")

                Matched_data['13'] = re.findall(Patterns["Publisher_IEEE_aRXIV_CVPR_3"], data_3)
                # print("IEEE Publisher: ", end=" ")
                # print(Matched_data['13']) if len(Matched_data['13']) else print("No match")

                Matched_data['14'] = re.findall(Patterns["Pages_IEEE_ARXIV_CVPR_3"], data_3)
                # print("IEEE Pages: ", end=" ")
                # print(Matched_data['14']) if len(Matched_data['14']) else print("No match")


                paper_format = None
                information = init_dict()
                if len(Matched_data['4']) or len(Matched_data['5']):
                    paper_format = "ACL/M"
                    information = get_information(Matched_data,information, paper_format)
                    
                else:
                    paper_format = "IEEE/ARXIV/CVPR"
                    information['author'] = data_1
                    print(f'TITLE', Matched_data['8'])
                    if len(Matched_data['8'])>=2:
                        if len(Matched_data['8'][1]):
                            information['title'] = Matched_data['8'][1][2]
                    if len(Matched_data['8'])>=5:
                        if len(Matched_data['8'][4]):
                            information['title'] += Matched_data['8'][4][1]
                            information['title'] += Matched_data['8'][4][2]
                    if len(Matched_data['14']):
                        information['Pages'] = Matched_data['14'][0]
                    if len(Matched_data['13']):
                        information['publisher'] = Matched_data['13'][0]

                print("-----------------------------------------")
                print(information)
                print("-----------------------------------------")
                input("Press Enter to continue...")



            tree = ET.ElementTree(root)
            ET.indent(tree, space="\t", level=0)
            tree.write('ACL_bbl.xml', encoding='utf-8', xml_declaration=True)

