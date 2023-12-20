from brain_games.utility import calculator
from random import randint, choice
from typing import Tuple

description = 'What is the result of the expression?'


def get_qna_pair() -> Tuple[str, str]:
    """Generates a mathematical expression with add, sub. and mult. operations
    User needs to find out the result to the given expression"""

    first_number = randint(1, 30)
    second_number = randint(1, 30)
    operator = choice(['+', '-', '*'])

    result = calculator.operate(first_number,
                                second_number,
                                operator)

    question = f'{str(first_number)} {operator} {str(second_number)}'
    answer = result  # eval('__import__("os").system("echo hello, hexlet!")')

    return question, str(answer)
