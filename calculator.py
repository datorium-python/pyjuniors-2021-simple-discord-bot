def get_operation(expression):

    operation = None

    if '+' in expression:
        operation = '+'

    elif '-' in expression:
        operation = '-'

    elif '*' in expression:
        operation = '*'

    elif '/' in expression:
        operation = '/'

    return operation


def calculate(number_1, number_2, operation):

    result = None

    if operation == '+':
        result = number_1 + number_2

    elif operation == '-':
        result = number_1 - number_2

    elif operation == '*':
        result = number_1 * number_2

    elif operation == '/':
        result = number_1 / number_2

    return result