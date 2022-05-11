import csv

# open file
data = open('example.csv', encoding='utf-8')
# csv read
csv_data = csv.reader(data)
# reformat it into a python object i.e list of lists
data_lines = list(csv_data)
# total number of rows
print(len(data_lines))
# column header
print(data_lines[0])
# grab email of the tenth datapoint
print(data_lines[10][3])
# grab all emails
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])
print(len(all_emails))
# ----------------------------------------
# Saving to CSV file
# new line is an empty string
file_to_save = open('to_save_file2.csv', mode='w', newline='')
# semicolon and tabs can also be provided as delimiters
csv_writer = csv.writer(file_to_save, delimiter=',')
csv_writer.writerow(['ch1', 'ch2', 'ch3'])
csv_writer.writerows([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
file_to_save.close()
# appending to an existing file
file_to_save = open('to_save_file2.csv', mode='a', newline='')
csv_writer = csv.writer(file_to_save, delimiter=',')
csv_writer.writerows([['j', 'k', 'l'], ['m', 'n', 'o']])
file_to_save.close()
