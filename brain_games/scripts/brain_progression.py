from brain_games import logic
from math import gcd
from random import randint, choice


def main():

    qna_pair = {}

    for i in range(3):
        random_number = randint(1, 15)
        step = randint(2, 5)

        sequence = []
        for n in range(10):
            sequence += [random_number + step * n]

        missing_number = choice(sequence)

        question = ' '.join((str(n) if n != missing_number else '..') for n in sequence)  # kinda messy ngl
        answer = missing_number

        qna_pair[str(question)] = str(answer)

    logic.ask_question(qna=qna_pair,
                       title='What number is missing in the progression?')
