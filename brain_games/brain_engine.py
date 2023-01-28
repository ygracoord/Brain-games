import prompt

from brain_games.cli import welcome_user


def playing(kind_of_game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(kind_of_game.TITLE)

    for _ in range(3):
        question, success_answer = kind_of_game.entry_data()
        print(f'Question: {question}')
        user_answer = int(prompt.secret('Your answer: '))

        if user_answer == success_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{success_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
