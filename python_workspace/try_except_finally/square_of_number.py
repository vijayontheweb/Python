'''
Simple Script
'''

IS_RETRY = True
while IS_RETRY:
    try:
        number = int(input('Enter a number?'))
    except ValueError:
        print('Sorry! Not a number. Please retry..')
    else:
        print('Yay! Your number is valid')
        print('Square of {} is {}'.format(number, number**2))
        IS_RETRY = False
    finally:
        print('I always run!')
