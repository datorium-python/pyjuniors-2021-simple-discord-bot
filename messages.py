import random


def say_hello():

    greetings = ['Hi', 'Hello', 'Čau', 'Sveiki']
    message_text = random.choice(greetings)

    return message_text


def spam(message_text):

    message_parts = message_text.split(' ')
    amount = int(message_parts[1])
    message_text = ' '.join(message_parts[2:])

    return amount, message_text


def calc(message_text):

    from calculator import get_operation, calculate

    expression = message_text.replace('!calc ', '')
    operation = get_operation(expression)

    numbers = expression.split(operation)
    result = calculate(int(numbers[0]), int(numbers[1]), operation)

    return result

