def operate(first_number, second_number, operator):
    match operator:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case _:
            print('Unsupported operation!')
            return None

    return result
