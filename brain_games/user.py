import prompt


def ask_for_name():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
