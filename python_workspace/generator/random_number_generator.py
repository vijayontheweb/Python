'''
    Create a generator that yields "n" random numbers between low and a high number
'''
import random


def generate_random(low, high, count):
    for index in range(count):
        yield random.randint(low, high)


print(list(generate_random(5, 25, 5)))
for i in generate_random(5, 25, 5):
    print(i)
