import math
import prompt
import random

TITLE = 'Find the greatest common divisor of given numbers.'


def entry_data():
    number1, number2 = random.randint(1, 50), random.randint(1, 50)
    user_answer = prompt.string(f'Question: {number1} {number2} ')
    success_answer = math.gcd(number1, number2)
    return user_answer, str(success_answer)
