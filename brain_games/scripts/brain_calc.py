from brain_games import logic
from random import randint, choice


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        first = randint(1, 50)
        second = randint(1, 50)
        operator = choice(['+', '-', '*'])

        question = f'{str(first)} {operator} {str(second)}'
        answer = eval(question)

        qna_pair[str(question)] = str(answer)

    logic.ask_question(qna=qna_pair,
                       title='What is the result of the expression?')
