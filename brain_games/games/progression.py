from random import randint, choice


description = 'What number is missing in the progression?'


def get_qna_pair():
    random_number = randint(1, 15)
    step = randint(2, 5)

    sequence = []
    sequence_length = 10
    for index in range(sequence_length):
        sequence += [random_number + step * index]

    missing_number = choice(sequence)

    question = ' '.join(
        (str(n) if n != missing_number else '..') for n in sequence)
    answer = missing_number

    return question, answer
