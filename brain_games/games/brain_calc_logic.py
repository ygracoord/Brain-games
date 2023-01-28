import random

TITLE = 'What is the result of the expression?'


def entry_data():
    number1, number2 = random.randint(1, 30), random.randint(1, 30)
    operator = random.choice(['+', '-', '*'])
    question = f'{number1} {operator} {number2}'
    success_answer = calculate_result(number1, number2, operator)
    return question, success_answer


def calculate_result(number1, number2, operator):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return result
