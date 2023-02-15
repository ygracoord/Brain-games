import random
from operator import add, sub, mul

TITLE = 'What is the result of the expression?'
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_question_and_answer():
    number_1, number_2 = random.randint(1, 30), random.randint(1, 30)
    operation_name, operation_method = random.choice(OPERATIONS)
    question = f'{number_1} {operation_name} {number_2}'
    success_answer = operation_method(number_1, number_2)
    return question, str(success_answer)
