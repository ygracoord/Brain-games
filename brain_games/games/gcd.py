import math
import random

TITLE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1, number2 = random.randint(1, 50), random.randint(1, 50)
    question = f'{number1} {number2}'
    success_answer = math.gcd(number1, number2)
    return question, str(success_answer)
