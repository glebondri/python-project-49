from brain_games.utility import prime
from random import randint
from typing import Tuple

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_qna_pair() -> Tuple[str, str]:
    """Generates a random number in range from one to thirty
    User needs to find out whether the given number is prime or not"""

    question = randint(1, 30)
    answer = 'yes' if prime.is_prime_number(question) else 'no'

    return str(question), answer
