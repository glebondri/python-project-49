from brain_games import user
from brain_games.titles import QUESTION, WRONG_ANSWER, TRY_AGAIN


def ask_to_answer(game):
    print('Welcome to the Brain Games!')

    username = user.ask_for_name()
    print(f'Hello, {username}!')

    print(game.description)

    for attempt in range(3):
        question, answer = game.get_qna_pair()

        user_answer = input(QUESTION.format(str(question)))

        if str(user_answer) != str(answer):
            print(WRONG_ANSWER.format(user_answer, answer))
            print(TRY_AGAIN.format(username))
            exit(0)

        print('Correct!')

    print(f'Congratulations, {username}!')
