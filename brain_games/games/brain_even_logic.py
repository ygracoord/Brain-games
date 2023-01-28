import random
import prompt

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def entry_data():
    random_num = random.randint(1, 100)
    user_answer = prompt.secret(f'Question: {random_num} ')

    if random_num % 2 == 0:
        success_answer = 'yes'
    else:
        success_answer = 'no'
    return user_answer, str(success_answer)
