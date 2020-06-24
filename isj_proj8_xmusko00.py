#!/usr/bin/env python3

'''
Katerina Muskova, xmusko00
isj_proj8
Kveten, 2019
'''


def first_with_given_key(iterable, key = lambda arg: arg):
    """returns first with given key"""

    memory = set()
    for it in iter(iterable):
        if key(it) not in memory:
            memory.add(key(it))
            yield it


if __name__ == "__main__":
    import doctest
    doctest.testmod()
