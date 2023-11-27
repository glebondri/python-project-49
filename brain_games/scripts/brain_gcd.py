from brain_games import logic
from brain_games import titles
from math import gcd as greatest_common_divisor
from random import randrange


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        first = randrange(1, 50, 2)
        second = randrange(1, 50, 2)

        question = f'{str(first)} {str(second)}'
        answer = greatest_common_divisor(first, second)

        qna_pair[question] = answer

    logic.ask_questions(qna=qna_pair,
                        title=titles.BRAIN.GCD)
