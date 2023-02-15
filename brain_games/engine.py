import prompt

ATTEMPTS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.TITLE)

    for _ in range(ATTEMPTS):
        question, success_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != success_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{success_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
