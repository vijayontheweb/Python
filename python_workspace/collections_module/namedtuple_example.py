from collections import namedtuple

Human = namedtuple('Human', ['age', 'height', 'weight'])
vijay = Human(39, 172, 80)
print(vijay)
print(vijay.age)
print(vijay[2])
priya = Human(age='35', height=160, weight=65)
print(priya)
print(type(priya))
