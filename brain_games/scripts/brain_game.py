#!usr/bin/env python3

from ..cli import welcome_user


def main():
    print('Welcome to the Brain Games!')

    username = welcome_user()

    print(f'Hello, {username}!')
