from one import function1


def function2():
    print('function1 called from two.py')


print('top level called from two.py')
function1()

if __name__ == "__main__":
    print('two.py is called DIRECTLY')
else:
    print('two.py is IMPORTED')
