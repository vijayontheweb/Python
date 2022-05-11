import PyPDF2

# READING FROM PDF
# rb stands for read binary
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(type(pdf_reader))
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()

# GRAB A PAGE AND WRITING TO ANOTHER PDF
f1 = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f1)
page_one = pdf_reader.getPage(0)
f2 = open('Output_file.pdf', 'wb')
pdf_writer = PyPDF2.PdfFileWriter()
print(type(pdf_writer))
pdf_writer.addPage(page_one)
pdf_writer.write(f2)
f2.close()

# GRAB ALL TEXT FROM PDF
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(type(pdf_reader))
print(pdf_reader.numPages)
all_page_texts = []
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    page_text = page.extractText()
    all_page_texts.append(page_text)
# Array of page texts for each page
print(all_page_texts)
f.close()
