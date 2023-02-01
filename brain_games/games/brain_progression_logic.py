import random
import prompt

TITLE = 'What number is missing in the progression?'


def entry_data():
    progression_list = []
    start, finish = random.randint(1, 10), random.randint(100, 110)
    random_step = random.randint(1, 5)

    for i in range(start, finish, random_step):
        progression_list.append(str(i))

        if len(progression_list) == 10:
            missed_elem = random.randint(0, len(progression_list) - 1)
            success_answer = str(progression_list[missed_elem])
            progression_list[missed_elem] = '..'
            final_list = ' '.join(progression_list[:10])
            user_answer = prompt.string(f'Question: {final_list} ')
            return user_answer, success_answer
