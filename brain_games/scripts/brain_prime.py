from brain_games import logic
from brain_games.utility import randomizer, prime


def main():

    qna_pair = {}  # dict of 'questions 'n' answers'

    for i in range(3):
        question = randomizer.unique(2, 59)
        answer = 'yes' if prime.is_prime_number(question) else 'no'

        qna_pair[str(question)] = answer

    logic.ask_question(qna=qna_pair,
                       title='Answer "yes" if given number is prime. Otherwise answer "no".')
