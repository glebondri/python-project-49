# def ask_question(question, answer):
#     user_answer = input(f'Question: {question}\nYour answer: ')
#
#     if user_answer != answer:
#         print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
#         return None
#
#     print('Correct!')
#
#     return True


def ask_question(title, username, qna):

    def unpack(dictonary, index):
        return index, dictonary[index]

    print(title)

    for q in qna:
        question, answer = unpack(qna, q)
        user_answer = input(f'Question: {question}\nYour answer: ')

        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {username}!")
            exit(0)

        print('Correct!')

    print(f'Congratulations, {username}!')
