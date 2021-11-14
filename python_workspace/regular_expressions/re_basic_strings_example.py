
import re
text = "The agent's phone number is 444-555-6666. Call soon!"
print('phone' in text)  # returns true

'''
re.search function takes a pattern, search the text and returns the first match object. 
And if no pattern is found, none is returned
If there are multiple matches in the string, re.search() would only get the first match
re.findall() will find just the list all the matches indicating strings that matched
re.finditer() iterates through the text and then returns each match object that's found
'''
pattern = "number"
# <re.Match object; span=(18, 24), match='number'>
print(re.search(pattern, text))
match = re.search(pattern, text)
print(match.span())  # (18, 24) -> returns the actual index location of the span
print(match.start())  # 18 -> returns the starting index of the span
print(match.end())  # 24 -> returns the ending index of the span

pattern = "notexist"
# None  -> We dont get back anything because there is no match
print(re.search(pattern, text))

text = "my phone once, my phone twice"
pattern = "phone"
matches = re.findall(pattern, text)
print(matches)  # ['phone', 'phone'] -> returns the actual text that matched
print(len(matches))  # 2 -> how many matches
for match in matches:
    print(match)
for match in re.finditer(pattern, text):  # iterates through the match object
    # first itertion -> <re.Match object; span=(3, 8), match='phone'>
    # second iteration -> <re.Match object; span=(18, 23), match='phone'>
    print(match)
    print(match.span())  # returns the actual index location of the span
    print(match.group())  # returns the actual text that matched
