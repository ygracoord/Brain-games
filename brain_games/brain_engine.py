from brain_games.cli import welcome_user


def run_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.TITLE)

    for _ in range(3):
        user_answer, success_answer = game.entry_data()
        print(f'Your answer: {user_answer}')

        if user_answer == success_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{success_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
