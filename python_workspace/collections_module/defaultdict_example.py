from collections import defaultdict

normal_dict = {'a': 10}
print(normal_dict)
print(normal_dict['a'])
'''
    Normal dictionary will throw KeyError
'''
# print(normal_dict['b'])
'''
    Default dictionary will NOT throw KeyError. Instead it returns default value
    where 0 is the default value for non-existing key
'''
default_dict = defaultdict(lambda: 0)
print(default_dict['WRONG_KEY'])
