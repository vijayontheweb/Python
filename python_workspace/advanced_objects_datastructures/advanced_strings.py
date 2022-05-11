s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())
# find the total count of O's
print(s.count('o'))
# find the first index of O
print(s.find('o'))
# Centres hello world within hyphens having total length of 20
print(s.center(20, '-'))
print('hello\tvijay'.expandtabs())
# is alphanumeric
print(s.isalnum())
# is alphabetic
print(s.isalpha())
# is lowercase
print(s.islower())
# is whitespace
print(s.isspace())
# is title
print(s.istitle())
# is upper
print(s.isupper())
# is ends with d
print(s.endswith('d'))
# split at every occurance of character
print('eastorwestindiaisthebest'.split('s'))
# split at first occurance of character
print('eastorwestindiaisthebest'.partition('s'))
