from random import randint, choice
from typing import Tuple


description = 'What number is missing in the progression?'


def get_qna_pair() -> Tuple[str, str]:
    """Generates an arithmetic sequence with a missing number in
    User needs to find out """

    random_number = randint(1, 15)
    step = randint(2, 5)

    sequence = []
    sequence_length = 10
    for index in range(sequence_length):
        sequence += [random_number + step * index]

    missing_number = choice(sequence)

    question = ' '.join(
        list(map(lambda x: str(x) if x != missing_number else '..', sequence)))
    answer = missing_number

    return question, str(answer)
