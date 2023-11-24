from brain_games import user


def ask_question(title, qna):

    def unpack(dictonary, index):
        return index, dictonary[index]

    username = user.ask_for_name()

    if len(qna) > 1:  # is there is anything to ask?
        print(title)

        for q in qna:
            question, answer = unpack(qna, q)
            user_answer = input(f'Question: {question}\nYour answer: ')

            if user_answer != answer:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {username}!")
                exit(0)

            print('Correct!')

        print(f'Congratulations, {username}!')

    else:
        print("I don't know what to ask you!")
