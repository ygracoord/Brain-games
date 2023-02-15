import random

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_num = random.randint(1, 100)
    question = f'{random_num}'
    success_answer = 'yes' if random_num % 2 == 0 else 'no'
    return question, success_answer
