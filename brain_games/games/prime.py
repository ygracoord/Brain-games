import random

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(-100, 100)
    success_answer = 'yes' if is_prime(question) else 'no'
    return question, success_answer
