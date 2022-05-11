'''
Wildcard acts as a placement that will match any character
'''
import re
# <re.Match object; span=(4, 7), match='dog'>
print(re.search(r'cat|dog', "The dog is here"))
# wildcard period(.) meaning anything here
# ['cat', 'hat', 'lat']
print(re.findall(r'.at', 'The cat with the hat splat there'))
# wildcard caret(^) meaning starts with
# ['1']
print(re.findall(r'^\d', '1 is a number'))
# wildcard dollar($) meaning ends with
# ['2']
print(re.findall(r'\d$', 'The number is 2'))
# EXCLUSION - wildcard caret(^) used in conjunction with square brackets[]
phrase = 'There are 3 cases in 4 cities since 2 days'
exclude_pattern = r'[^\d]+'
# ['There are ', ' cases in ', ' cities since ', ' days']
print(re.findall(exclude_pattern, phrase))
phrase = 'There are 3 cases in 4 cities since 2 days'
exclude_pattern = r'[^\d\s]+'
# ['There', 'are', 'cases', 'in', 'cities', 'since', 'days']
print(re.findall(exclude_pattern, phrase))
punctuation_phrase = 'This is a string! But it has punctuation. How can we remove it?'
exclude_pattern = r'[^!.?\s]+'
# ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']
print(re.findall(exclude_pattern, phrase))
sentence = re.findall(exclude_pattern, phrase)
# This is a string But it has punctuation How can we remove it
print(' '.join(sentence))
hyphen_phrase = 'This sentence has some hyphen-words. Find them and collect them cow-boy!!'
include_pattern = r'\w+-\w+'
include_pattern_with_group = r'[\w]+-[\w]+'
# ['hyphen-words', 'cow-boy']
print(re.findall(include_pattern, hyphen_phrase))
# ['hyphen-words', 'cow-boy']
print(re.findall(include_pattern_with_group, hyphen_phrase))
partial_match_phrase1 = 'Would you like to have lemontea'
partial_match_phrase2 = 'Would you like to have gingertea'
partial_match_phrase3 = 'Would you like to have greentea'
include_pattern = r'(lemon|ginger|green)tea'
# <re.Match object; span=(23, 31), match='lemontea'>
print(re.search(include_pattern, partial_match_phrase1))
# <re.Match object; span=(23, 32), match='gingertea'>
print(re.search(include_pattern, partial_match_phrase2))
# <re.Match object; span=(23, 31), match='greentea'>
print(re.search(include_pattern, partial_match_phrase3))
