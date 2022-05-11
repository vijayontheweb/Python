'''
Similar to list comprehension, dictionary datatypes also support their own version of comprehension
What if you want to assign keys that are not based on their values? zip can help
'''
# dictionary comprehension
d = {x: x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(d)
# dictionary comprehension with zip
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
d = {key: val for key, val in zip(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], range(10))}
print(d)
for item in d.items():
    # ('a', 0)
    # ('b', 1)...
    print(item)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
