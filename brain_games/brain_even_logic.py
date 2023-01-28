import random
import prompt

from brain_games.cli import welcome_user


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0

    while index < 3:
        random_num = random.randint(1, 100)

        if random_num % 2 == 0:
            user_answer = prompt.secret(f'Question: {random_num} ')
            if user_answer == 'yes':
                print(f'Your answer: {user_answer}', 'Correct!', sep='\n')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f'Lets try again, {name}!')
                return
        else:
            user_answer = prompt.secret(f'Question: {random_num} ')
            if user_answer == 'no':
                print(f'Your answer: {user_answer}', 'Correct!', sep='\n')
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f'Lets try again, {name}!')
                return
        index += 1
    print(f'Congratulations, {name}!')
