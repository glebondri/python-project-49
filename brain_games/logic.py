from brain_games import user
from brain_games.titles import QUESTION, WRONG_ANSWER, TRY_AGAIN


def ask_questions(title, qna):

    def unpack(dictonary, index):
        return index, dictonary[index]

    username = user.ask_for_name()

    if len(qna) > 1:  # is there is anything to ask?
        print(title)

        for q in qna:
            question, answer = unpack(qna, q)
            user_answer = input(QUESTION.format(question))

            if user_answer != answer:
                print(WRONG_ANSWER.format(user_answer, answer))
                print(TRY_AGAIN.format(username))
                exit(0)

            print('Correct!')

        print(f'Congratulations, {username}!')

    else:
        print("I don't know what to ask you!")
