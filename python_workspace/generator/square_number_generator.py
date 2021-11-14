'''
    Create a generator that generates squares of numbers up to some number N
'''


def square(num):
    for index in range(num):
        yield index**2


print(list(square(5)))
for i in square(5):
    print(i)
