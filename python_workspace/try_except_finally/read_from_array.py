for i in ['a', 'b', 'c']:
    try:
        number = int(i)
    except TypeError:
        print('Sorry! Not a number. You got TypeError')
    except OSError:
        print('Sorry! Not a number. You got OSError')
    except:
        print('Sorry! Not a number. You got an error')
    else:
        print(i**2)
    finally:
        print('I always run!')
