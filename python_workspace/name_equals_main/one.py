def function1():
    print('function1 called from one.py')


print('top level called from one.py')

if __name__ == "__main__":
    print('one.py is called DIRECTLY')
else:
    print('one.py is IMPORTED')
