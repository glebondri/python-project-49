#!usr/bin/env python3

from brain_games import user


def main():
    print('Welcome to the Brain Games!')

    username = user.ask_for_name()

    print(f'Hello, {username}!')
