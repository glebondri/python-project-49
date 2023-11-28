from brain_games import logic
from brain_games import titles
from brain_games.utility import randomizer


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        question = randomizer.unique(1, 6)
        answer = 'yes' if question % 2 == 0 else 'no'

        qna_pair[question] = answer

    logic.ask_questions(qna=qna_pair,
                        title=titles.BRAIN.EVEN)
