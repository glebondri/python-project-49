from brain_games import logic
from brain_games import titles
from brain_games.utility import randomizer
from random import randint, choice


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        random_number = randomizer.unique(1, 15)
        step = randint(2, 5)

        sequence = []
        sequence_length = 10
        for index in range(sequence_length):
            sequence += [random_number + step * index]

        missing_number = choice(sequence)

        question = ' '.join(
            (str(n) if n != missing_number else '..') for n in sequence)
        answer = missing_number

        qna_pair[question] = answer

    logic.ask_questions(qna=qna_pair,
                        title=titles.PROGRESSION)
