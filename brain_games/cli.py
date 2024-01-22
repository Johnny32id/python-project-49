import prompt


def welcome_user():
    '''greets the player'''
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
