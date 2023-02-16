import random

TITLE = 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    finish = (start + 10 * step)
    progression = list(map(str, range(start, finish, step)))
    missed_elem = random.randint(0, len(progression) - 1)
    success_answer = str(progression[missed_elem])
    progression[missed_elem] = '..'
    question = ' '.join(progression)
    return question, success_answer
