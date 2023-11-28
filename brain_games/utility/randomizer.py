from random import randint

memory = []


def unique(first, last):  # used to generate unique random numbers
    global memory

    random_number = randint(first, last)
    if random_number in memory:
        try:
            return unique(first, last)
        except RecursionError:
            print("Seems, I can't offer you more numbers than you asked for!")
            exit(0)

    memory += [random_number]
    return random_number
