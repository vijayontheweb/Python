'''
Random Module	- Pseudo Random Number Generators
Allows us to create random numbers and we can even set a SEED to produce the same random set every time
Setting a SEED allows us to start from a seeded pseudorandom number generator, which means the same random numbers will
show up in a series
'''

# random.randint() -> Return random integer in range [a,b] including both end points
import random

random.seed(101)		# Seed number is completely arbitrary
# 74
print(f'SEED DRIVEN PREDICATABLE RANDOM -> {random.randint(0, 100)}')
# 24
print(f'SEED DRIVEN PREDICATABLE RANDOM -> {random.randint(0, 100)}')
# 69
print(f'SEED DRIVEN PREDICATABLE RANDOM -> {random.randint(0, 100)}')
# Using Seed, the same random numbers are generated

# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
mylist = list(range(0, 20))
# 16	i.e grab one item from the list
print(f'ONE RANDOM -> {random.choice(mylist)}')
# grab multiple items from the list
# Allow yourself to pick the same number more than once. Sampling with replacement
print(
    f'MULTI RANDOM W/ REPLACEMENT -> {random.choices(population=mylist, k=10)}')        # [4,4,5,13,4,19,1,3,1,15]
# Allow yourself to pick the same number ONLY once. Sampling without replacement
print(
    f'MULTI RANDOM W/O REPLACEMENT -> {random.sample(population=mylist, k=10)}')        # [4,7,5,13,1,19,2,3,14,15]

print(f'BEFORE SHUFFLE -> {mylist}')
random.shuffle(mylist)      # Shuffle list inplace permanently
print(f'AFTER SHUFFLE -> {mylist}')
# Continuous/uniform distribution. Every number in range has same likelihood of being chosen.	 Floating point allowed
# 74.44690143237648
print(f'UNIFORM DISTRIBUTION -> {random.uniform(a=0, b=100)}')
# Normal/Gaussian Distribution
# -1.7665992795896235
print(f'GAUSSIAN DISTRIBUTION -> {random.gauss(mu=0, sigma=1)}')
