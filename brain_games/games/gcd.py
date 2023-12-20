from random import randint
from math import gcd as greatest_common_divisor
from typing import Tuple

description = 'Find the greatest common divisor of given numbers.'


def get_qna_pair() -> Tuple[str, str]:
    """Generates a two random numbers
    User needs to find out the greatest common divisor of two given numbers"""

    first_number = randint(1, 50)
    second_number = randint(1, 50)

    question = f'{str(first_number)} {str(second_number)}'
    answer = greatest_common_divisor(first_number, second_number)

    return question, str(answer)
