# # Group Name: Codemasters

from PyPDF2 import PdfFileReader
from pathlib import Path

from board import user_actions

x = int(input('Do you wish to add a pdf?\n1. YES\n2. NO'))

if x == 1:
    location = input('Enter directory')
    file_path = (Path.home() / f"{location}")
    try:
        pdf = PdfFileReader(file_path)
        with open('Code_writer.txt', 'a') as f:
            for page_num in range(pdf.numPages):
                pageObj = pdf.getPage(page_num)

                try:
                    txt = pageObj.extractText()
                except:
                    pass
                else:
                    f.write('Page {0}\n'.format(page_num + 1))
                    f.write(txt)
            f.close()
    except:
        print('The directory is inaccurate or the extension is inaccurate')


elif x == 2:
    with open('Code_writer.txt', 'a') as f:
        f.write(user_actions)
        f.close()