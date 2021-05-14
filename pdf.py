import PyPDF4  # może wyciągnąć sam TEXT
import os

pdfFile = open('meetingminutes1.pdf', 'rb')  # readbinary
reader = PyPDF4.PdfFileReader(pdfFile)

# print(reader.numPages)
page = reader.getPage(0)
# print(page)

extract = page.extractText()
# print(extract)

for p in range(reader.numPages):
    print(reader.getPage(p).extractText())
pdfFile.close()

'''
łączenie pdf w pythonie
'''
pdfFile1 = open('meetingminutes1.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF4.PdfFileReader(pdfFile1)
reader2 = PyPDF4.PdfFileReader(pdfFile2)

writer = PyPDF4.PdfFileWriter()
for p in range(reader1.numPages):
    page = reader1.getPage(p)
    writer.addPage(page)
for p in range(reader2.numPages):
    page = reader2.getPage(p)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile1.close()
pdfFile2.close()