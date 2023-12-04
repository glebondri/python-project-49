from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_qna_pair():
    question = randint(1, 10)
    answer = 'yes' if question % 2 == 0 else 'no'

    return question, answer
