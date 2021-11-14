def inline_list(number):
    num_list = []
    for index in range(number):
        num_list.append(index)
    return num_list


def list_generator(number):
    for index in range(number):
        yield index


print(f'Inline list = {inline_list(10)}')
generator1 = list_generator(10)
print(f'Generator object = {generator1}')
print(f'Generator list = {list(generator1)}')
print(f'Generator list again = {list(generator1)}')
print('Iterating over Generator:')
generator2 = list_generator(10)
for index in generator2:
    print(index)
print('Using NEXT over Generator:')
generator3 = list_generator(5)
print(next(generator3))
print(next(generator3))
print(next(generator3))
print(next(generator3))
print(next(generator3))
'''
This will result in StopIteration error after yielding all the values

Traceback (most recent call last):
  File "yield_example.py", line 32, in <module>
    print(next(generator3))
StopIteration

'''
# print(next(generator3))

'''
ITER function - Converts objects that are iterable into iterator themselves
String object naturally doesn't support ITER.
Therefore you wont be able to call NEXT function over a String object 
ITER function converts a String into a generator so that we can iterate over it
'''
word = 'hello'
print('Using for loop over String object:')
for letter in word:
    print(letter)
print('Using ITER over String object:')
iter_word = iter(word)
print(next(iter_word))
print(next(iter_word))
print(next(iter_word))
print(next(iter_word))
print(next(iter_word))
