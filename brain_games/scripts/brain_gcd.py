from brain_games import logic
from brain_games import titles
from brain_games.utility import randomizer
from math import gcd as greatest_common_divisor


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        first_number = randomizer.unique(1, 50)
        second_number = randomizer.unique(1, 50)

        question = f'{str(first_number)} {str(second_number)}'
        answer = greatest_common_divisor(first_number, second_number)

        qna_pair[question] = answer

    logic.ask_questions(qna=qna_pair,
                        title=titles.BRAIN.GCD)
