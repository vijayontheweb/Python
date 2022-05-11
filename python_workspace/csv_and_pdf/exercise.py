'''
Task One: Use Python to extract the Google Drive link from the .csv file. 
(Hint: Its along the diagonal from top left to bottom right).
Task Two: Download the PDF from the Google Drive link (we already downloaded it 
for you just in case you can't download from Google Drive) and find the phone number 
that is in the document. Note: There are different ways of formatting a phone number!
'''
import csv
import re
import PyPDF2

# Task One
# open file
data = open('find_the_link.csv', encoding='utf-8')
# csv read
csv_data = csv.reader(data)
# reformat it into a python object i.e list of lists
data_lines = list(csv_data)
# APPROACH #1
line_count = len(data_lines)
url = []
for index in range(line_count):
    url.append(data_lines[index][index])
print(''.join(url))
# APPROACH #2
url_str = ''
for row_num, data_line in enumerate(data_lines):
    url_str += data_line[row_num]
print(url_str)


# Task Two
# GRAB ALL TEXT FROM PDF
f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
all_page_texts = ''
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    page_text = page.extractText()
    all_page_texts += page_text
# Array of page texts for each page
# print(all_page_texts)
f.close()
# Find Phone Number
quantified_phone_pattern = r"\d{3}.\d{3}.\d{4}"
phone_match = re.findall(quantified_phone_pattern, all_page_texts)
print(phone_match)
