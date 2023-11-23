from random import randint

memory = []


def unique(first, last):
    global memory

    random_number = randint(first, last)
    if random_number in memory:
        return unique(first, last)

    memory += [random_number]
    return random_number
