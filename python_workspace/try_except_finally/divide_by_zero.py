try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('Sorry! You are dividing by zero. You got ZeroDivisionError')
except:
    print('Sorry! You are dividing by zero. You got an error')
else:
    print('Division is valid!')
finally:
    print('All Done!')
