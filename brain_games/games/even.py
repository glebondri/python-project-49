from random import randint
from typing import Tuple


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_qna_pair() -> Tuple[str, str]:
    """Generates a random number in range from zero to ten
    User needs to find out whether the given number is even or not"""

    question = randint(1, 10)
    answer = 'yes' if question % 2 == 0 else 'no'

    return str(question), answer
