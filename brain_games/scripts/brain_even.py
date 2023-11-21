from brain_games import user, logic, randomizer


def main():
    name = user.ask_for_name()

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        question = randomizer.unique(1, 10)
        answer = 'yes' if question % 2 == 0 else 'no'

        qna_pair[str(question)] = answer

    logic.ask_question(username=name, qna=qna_pair,
                       title='Answer "yes" if the number is even, otherwise answer "no".')