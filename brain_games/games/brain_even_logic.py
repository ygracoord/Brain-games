import random

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def entry_data():
    random_num = random.randint(1, 100)
    user_answer = random_num
    if random_num % 2 == 0:
        success_answer = 'yes'
    else:
        success_answer = 'no'
    return user_answer, success_answer
