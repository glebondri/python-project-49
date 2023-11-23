from brain_games import logic
from math import gcd
from random import randint


def main():

    qna_pair = {}

    for i in range(3):
        first = randint(1, 50)
        second = randint(1, 50)

        question = f'{str(first)} {str(second)}'
        answer = gcd(first, second)

        qna_pair[str(question)] = str(answer)

    logic.ask_question(qna=qna_pair,
                       title='Find the greatest common divisor of given numbers.')