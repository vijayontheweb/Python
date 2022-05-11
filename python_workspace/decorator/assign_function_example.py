'''
We can actually assign a function to variables and execute that function off that variable
'''


def hello():
    return "hello vijay"


print(hello)
print(hello())
greet = hello
print(greet)
print(greet())
del hello
print(greet)
print(greet())
