from brain_games import logic
from brain_games import titles
from brain_games.utility import randomizer
from random import randint, choice


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        first_number = randomizer.unique(1, 50)
        second_number = randomizer.unique(1, 50)
        operator = choice(['+', '-', '*'])

        question = f'{str(first_number)} {operator} {str(second_number)}'
        answer = eval(question)

        qna_pair[str(question)] = str(answer)

    logic.ask_questions(qna=qna_pair,
                        title=titles.BRAIN.CALC)
