def operate(a, b, operator):
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
