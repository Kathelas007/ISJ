#!/usr/bin/env python3

'''
Katerina Muskova, xmusko00
isj_proj7
Duben, 2019
'''

import collections

my_counter = collections.Counter()

'''
def log_and_count(fnc, key, counts):
    def vnitrek:
        pass
'''

def log_and_count(*args, **kwargs):                        # argumenty dekoratoru
    if not (len(kwargs) == 2 or len(kwargs) == 1):
        raise Exception("Bad number of arguments")
    #poresit argumety a chybky

    def log_and_count_fnc(fnc):                            # funkce
        def inner(*arg_f, **kwargs_f):                     # puvodni funkce


            print("called " + fnc.__name__ + " with (", end='')

            if len(arg_f) == 1 or len(arg_f) == 2:
                print(str(arg_f[0]) + ",", end='')

            if len(arg_f) == 2:
                print(" " + str(arg_f[1]) + ")", end='')
            else:
                print(")", end='')

            print(" and ", end='')

            if len(kwargs_f) != 0:
               print(kwargs_f, end='')
            else:
                print("{}", end='')

            print('')

            ###########################

            c_key: str
            c_counter = kwargs["counts"]

            if("key" in kwargs.keys()):
                c_key = kwargs["key"]
            elif len(args) == 1:
                c_key = args[0]
            else:
                c_key = fnc.__name__

            if c_key in c_counter.keys():
                c_counter[c_key] +=1
            else:
                c_counter[c_key] = 1

            rtnVal = None
            return rtnVal
        return inner
    return log_and_count_fnc


@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b


@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b


if __name__ == "__main__":
    f3(3, 3)
    f3(1, 3)
    f3(3, 3)

    print(my_counter)

