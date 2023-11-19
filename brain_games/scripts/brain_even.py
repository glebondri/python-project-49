import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name


def main():
    print('Welcome to the Brain Games!')

    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for attempt in range(3):
        random_number = randint(1, 10)

        user_answer = input(f'Question: {random_number}\nYour answer: ')
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
