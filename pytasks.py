# 1. Define a function, that takes string as argument and prints "Heelo, %arg%!"
def greet(name):
    if len(name) > 0 and type(name) == str:
        print('Hello {}!'.format(name))
greet('Mentor')
