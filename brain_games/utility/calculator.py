from typing import Optional


def operate(a: int, b: int, operator: str) -> Optional[int]:
    """Arithmetic operation over two numbers
    :param a: First number
    :param b: Second number
    :param operator: Arithmetic operator (add, subtract or multiply)
    :return: Result of arithmetic operation (None if operator is invalid)"""

    match operator:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case _:
            print('Unsupported operation!')
            return None

    return result
