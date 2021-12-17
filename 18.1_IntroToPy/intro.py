def greet(person=None):
    if person == None:
        name = input('What is your name?')
        return f'Hello there, {name}!'
    else: return f'Hello there, {person}!'