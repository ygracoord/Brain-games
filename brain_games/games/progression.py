import random
import prompt

TITLE = 'What number is missing in the progression?'


def get_question_and_answer():
    progression_list = []
    start, finish = random.randint(1, 10), random.randint(100, 110)
    random_step = random.randint(1, 5)

    for i in range(start, finish, random_step):
        progression_list.append(str(i))

        if len(progression_list) == 10:
            missed_elem = random.randint(0, len(progression_list) - 1)
            success_answer = str(progression_list[missed_elem])
            progression_list[missed_elem] = '..'
            final_progression = ' '.join(progression_list[:10])
            print(f'Question: {final_progression}')
            user_answer = prompt.string('Your answer: ')
            return user_answer, success_answer
