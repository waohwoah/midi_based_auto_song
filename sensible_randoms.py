import random

history_list = list()


def non_repeated_randoms():
    global history_list
    history_list = history_list[1:]
    if len(history_list) is 0:
        history_list = random.sample(range(4), 4)
    return history_list[0]
