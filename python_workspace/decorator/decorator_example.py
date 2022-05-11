def decorate(original_func):
    def wrapped_func():
        print('Wrapper start')
        original_func()
        print('Wrapper finish')

    return wrapped_func


def original():
    print('I am original')


wrapped = decorate(original)
wrapped()
print('-------------------------------')

'''
We can also acheive the same using @ symbol
When we put this @<decorator function> on top of the original function
it wraps the original function similar to above example and returns
the wrapped function
If you dont want the decorator, simply comment it off i.e. ON/OFF switch
'''


@decorate
def another_original():
    print('I am another original')


another_original()
