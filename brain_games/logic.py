from brain_games import user
from brain_games.titles import QUESTION, WRONG_ANSWER, TRY_AGAIN
from types import ModuleType


def ask_to_answer(game: ModuleType) -> None:
    """Asks the user to answer three generated questions
    :param game: Module with game description and Q&A generation function"""

    print('Welcome to the Brain Games!')

    username = user.ask_for_name()
    print(f'Hello, {username}!')

    print(game.description)

    for attempt in range(3):
        question, answer = game.get_qna_pair()

        user_answer = input(QUESTION.format(question))

        if user_answer != answer:
            print(WRONG_ANSWER.format(user_answer, answer))
            print(TRY_AGAIN.format(username))
            exit(0)

        print('Correct!')

    print(f'Congratulations, {username}!')
