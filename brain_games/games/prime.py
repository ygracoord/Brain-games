import random

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    random_num = random.randint(-100, 100)
    question = random_num
    success_answer = 'yes' if is_prime(random_num) else 'no'
    return question, str(success_answer)
