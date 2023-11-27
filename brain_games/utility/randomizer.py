from random import randint

memory = []


def unique(first, last):  # used to generate unique random number
    global memory

    random_number = randint(first, last)
    if random_number in memory:
        return unique(first, last)

    memory += [random_number]
    return random_number
