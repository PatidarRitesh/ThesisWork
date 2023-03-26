# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import BytesIO, StringIO

# def convert_pdf(path, format, codec='utf-8', password=''):
#     rsrcmgr = PDFResourceManager()
#     # retstr = BytesIO()
#     retstr = StringIO()
#     laparams = LAParams()
    
#     if format == 'text':
#         device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
#     elif format == 'html':
#         device = HTMLConverter(rsrcmgr, retstr, laparams=laparams)
#     elif format == 'xml':
#         device = XMLConverter(rsrcmgr, retstr, laparams=laparams)
#     else:
#         raise ValueError('provide format, either text, html or xml!')
#     fp = open(path, 'rb')

#     interpreter = PDFPageInterpreter(rsrcmgr, device)

#     maxpages = 1
#     caching = True
#     pagenos=set()
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)

#     # print("retstr.getvalue() : ", retstr.getvalue())
#     text = retstr.getvalue()
#     fp.close()
#     device.close()
#     retstr.close()
#     return text



# print(convert_pdf('input11.pdf', format='xml'))


import os
import subprocess

# Define the input and output file paths
input_file = 'input.tex'
output_file = 'output.xml'

# Define the command to run LaTeXML
latexml_command = f'latexml --dest={output_file} {input_file}'

# Run the LaTeXML command using subprocess
try:
    subprocess.run(latexml_command, shell=True, check=True)
    print('LaTeX to XML conversion successful.')
except subprocess.CalledProcessError as e:
    print(f'Error running LaTeX to XML conversion: {e}')
