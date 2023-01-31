import random
import prompt

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
        if d * d > num:
            return 'yes'
    return 'no'


def entry_data():
    random_num = random.randint(2, 100)
    user_answer = prompt.secret(f'Question: {random_num} ')
    success_answer = is_prime(random_num)
    return user_answer, success_answer
