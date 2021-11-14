# Convert 1024 to binary and hexadecimal representation
num = 1024
# 0x400
print(hex(num))
# 0b10000000000
print(bin(num))
# Round 5.23222 to two decimal places
num = 5.23222
# 5.23
print(round(num, 2))
# Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
# False
print(s.islower())
# How many times does the letter 'w' show up in the string below
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
# 12
print(s.count('w'))
# Find the elements in set1 that are not in set2
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
# {2}
print(set1.difference(set2))
# Find all elements that are in either set
# {1, 2, 3, 5, 6, 7, 8}
print(set1.union(set2))
# Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension
d = {num: num**3 for num in range(5)}
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(d)
# Reverse the list below
list1 = [1, 2, 3, 4]
list1.reverse()
# [4, 3, 2, 1]
print(list1)
list2 = [3, 4, 2, 5, 1]
list2.sort()
# [1, 2, 3, 4, 5]
print(list2)
