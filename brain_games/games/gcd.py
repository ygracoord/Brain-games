import math
import prompt
import random

TITLE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1, number2 = random.randint(1, 50), random.randint(1, 50)
    print(f'Question: {number1} {number2}')
    user_answer = prompt.string('Your answer: ')
    success_answer = math.gcd(number1, number2)
    return user_answer, str(success_answer)
