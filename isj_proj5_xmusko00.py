#!/usr/bin/env python3

def gen_quiz(qpool: list, *indexes: int, altcodes='ABCDEF', quiz: list = None):

    if len(altcodes) > 6:
        altcodes = altcodes[:6]

    if quiz is None:
        quiz = []

    checked_ind = []

    if not indexes:
        checked_ind = []
    else:
        for ind_q in indexes:

            try:
                a = qpool[ind_q]
                checked_ind.append(ind_q)
            except IndexError:
                print("Ignoring index " + str(ind_q) + " - list index out of range")


    new_answs = list(
        [': '.join(map(str, x)) for x in zip(altcodes, qpool[ind_q][1])]
        for ind_q in checked_ind)

    return quiz + list(
        zip(list(qpool[ind_q][0] for ind_q in checked_ind), new_answs))
