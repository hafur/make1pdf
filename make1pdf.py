#!python

import PyPDF2
import os
import pyperclip
from datetime import date


path = pyperclip.paste()
print(path)
pdfWriter = PyPDF2.PdfFileWriter()


for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('pdf'):
        pdfFileObj = open(path + '\\' + entry.name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(pdfReader.numPages):
            print(pageNum)
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)


pdfOutputFile = open(path + '\\' + str(date.today().year) + str(date.today().month) + str(date.today().day) +
                     '_output.pdf',  'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFileObj.close()
