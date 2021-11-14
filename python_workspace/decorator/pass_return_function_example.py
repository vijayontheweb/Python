'''
Functions are objects that can be actaully passed into other objects
Return a function and execute them after we assign them to a variable
'''


def which_sound(animal):
    def lion():
        return "roar"

    def cat():
        return "meow"

    if(animal == 'lion'):
        return lion
    elif(animal == 'cat'):
        return cat


sound = which_sound('lion')
print(sound())
sound = which_sound('cat')
print(sound())

'''
Passing a function within another function
'''


def fish():
    return 'swim'


def cheetah():
    return 'run'


def move(action):
    print('I '+action())


animal = fish
move(animal)
animal = cheetah
move(animal)
