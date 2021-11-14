import re
text = "My phone number is 405-443-2343"
phone_pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
phone_match = re.search(phone_pattern, text)
print(phone_match)  # <re.Match object; span=(19, 31), match='405-443-2343'>

# We can use quantifiers to indicate repitition of the same character
quantified_phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_match = re.search(quantified_phone_pattern, text)
print(phone_match)  # <re.Match object; span=(19, 31), match='405-443-2343'>

'''
    We can use groups for any general tasks that involves grouping together regular expressions 
    and that allows us to later break them down
    compile - compiles together different regular expression pattern codes using parenthesis. 
    A parenthesis indicate group or pattern
    It takes multiple pattern codes and each pattern code is seperated with parenthesis as a group 
	and it compiles them into a single expression
    Later you could call the groupings individually	
'''
compiled_phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
phone_match = re.search(compiled_phone_pattern, text)
print(phone_match)  # <re.Match object; span=(19, 31), match='405-443-2343'>
print(phone_match.group())  # 405-443-2343
print(phone_match.group(1))  # 405
print(phone_match.group(2))  # 443
print(phone_match.group(3))  # 2343
# print(phone_match.group(4)) # Results in IndexError: no such group
