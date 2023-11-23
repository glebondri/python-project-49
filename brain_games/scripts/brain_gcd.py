from brain_games import logic
from math import gcd
from random import randrange


def main():

    qna_pair = {}

    for i in range(3):
        first = randrange(1, 50, 2)
        second = randrange(1, 50, 2)

        question = f'{str(first)} {str(second)}'
        answer = gcd(first, second)

        qna_pair[str(question)] = str(answer)

    logic.ask_question(qna=qna_pair,
                       title='Find the greatest common divisor of given numbers.')
