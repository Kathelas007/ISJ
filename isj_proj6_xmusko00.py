#!/usr/bin/env python3

'''
Katerina Muskova, xmusko00
isj_proj6
Duben, 2019
'''


class Polynomial:
    values: list

    def __init__(self, *args, **kwargs):
        self.values = []

        if len(args) == 0 and len(kwargs) == 0:  # no arguments
            self.values = [0]
            return

        if len(args) != 0 and len(kwargs) != 0:  # more argument, than expected
            raise ValueError('More arguments, than expected.')

        if len(kwargs) == 0:  # process args
            if len(args) == 1 and isinstance(args, tuple) and isinstance(args[0], list):  # x = Polynomial([2, 4, 6, 2])
                if all(isinstance(x, int) for x in args[0]):
                    self.values = list(x for x in args[0])
                    return
                else:
                    raise ValueError('Init arguments in list are expected to be int.')

            self.values = list(x for x in args)  # x = Polynomial(2, 4, 6, 2)

        else:  # process kwargs
            if not isinstance(kwargs, dict):
                raise ValueError("Kwargs are expected to be dict.")

            if not all(isinstance(x, int) for x in kwargs.values()):
                raise ValueError("Arguments are expected to be int.")

            if all(val == 0 for val in kwargs.values()):
                self.values = [0]
                return

                # replace x in keys
            kwargs = {int(key.replace('x', '')): int(val) for key, val in kwargs.items()}

            upperLimit = max(kwargs.keys())  # init self.values
            self.values = [0] * (upperLimit + 1)

            for key in kwargs.keys():  # copy values to self.values
                self.values[key] = kwargs[key]

            while self.values[-1] == 0:  # delete 0 from right
                del self.values[-1]

    def __str__(self):
        """Human readable form of Polynom"""

        if len(self.values) == 1 and self.values[0] == 0:
            return "0"

        ret_str = ""

        for ind, val in enumerate(reversed(self.values)):  # process everything exept null values and first value
            if val != 0 and ind != len(self.values) - 1:

                if val < 0:
                    ret_str += " - "
                else:
                    ret_str += " + "

                if abs(val) != 1:
                    ret_str += str(abs(val))

                ret_str += "x"

                if len(self.values) - ind - 1 != 1:
                    ret_str += "^" + str(len(self.values) - ind - 1)

        if ret_str.startswith(" + "):  # remove first +
            ret_str = ret_str[3:]

        if self.values[0] == 0:
            return ret_str.strip()

        if self.values[0] < 0:  # first index
            ret_str += " - "
        else:
            ret_str += " + "

        if ret_str.startswith(" + "):  # remove first " + "
            ret_str = ret_str[3:]

        return (ret_str + str(abs(self.values[0]))).strip()

    def __eq__(self, self2):
        """Oerator =="""

        return self.values == self2.values

    def __add__(self, self2):
        """Adding Polynomials"""

        if len(self.values) == len(self2.values):  # same lenght, just summarize
            return Polynomial(list(
                s + s2 for s, s2 in zip(self.values, self2.values)))

        tmp_list = list(
            s + s2 for s, s2 in zip(self.values, self2.values))  # summarize the same indexes

        sub = abs(len(self.values) - len(self2.values))

        if len(self.values) > len(self2.values):  # add the rest of longer list
            tmp_list.extend(self.values[-sub:])

        else:
            tmp_list.extend(self2.values[-sub:])

        return Polynomial(tmp_list)

    def multiply(self, suma_t: list):
        """Multiplies two lists"""
        '''Help function for __pow__()'''

        max_len = len(suma_t) + len(self.values)
        tmp_sum = [0] * max_len  # init tmp_sum

        for i, x in enumerate(suma_t):
            for j, y in enumerate(self.values):  # multiply
                tmp_sum[j + i] = tmp_sum[j + i] + y * x

        return tmp_sum

    def __pow__(self, power):
        """Power of Polynom"""

        if power < 0:  # error
            raise ValueError("Power must be positive")

        if power == 1:  # the same
            return self

        if power == 0:  # always 1
            return Polynomial(1)

        tmp_values = list(x for x in self.values)
        # other cases
        while power > 1:
            tmp_values = self.multiply(tmp_values)
            power -= 1

        return Polynomial(tmp_values)

    def derivative(self):
        """Derivative of Polynomial"""

        if len(self.values) == 1:
            return Polynomial(0)

        return Polynomial(list(
            ind * self.values[ind] for ind in range(1, len(self.values))
        ))

    def at_value(self, *nums: int):
        """Value of Polynomial in number"""
        """If two arguments appear, function returns diffrence of values"""

        sum_t = 0

        if len(nums) == 2:  # twp args
            for ind, val in enumerate(self.values):
                sum_t += val * (nums[1] ** ind) - val * (nums[0] ** ind)

            return sum_t

        if len(nums) == 1:  # one arg
            for ind, val in enumerate(self.values):
                sum_t += val * (nums[0] ** ind)

            return sum_t

        raise ValueError('Method at_value() expects one or two arguments.')


def test():
    assert str(Polynomial(0, 1, 0, -1, 4, -2, 0, 1, 3, 0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5, 1, 0, -1, 4, -2, 0, 1, 3, 0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3=-1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2, 0, 3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1) + Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1, 1, 1, 0]) + Polynomial(1, -1, 1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1, x1=1) ** 1) == "x - 1"
    assert str(Polynomial(x0=-1, x1=1) ** 2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1, x1=1)
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2, x1=3, x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
    pol5 = Polynomial([1, 0, -2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1, 3.6) == -23.92
    assert pol5.at_value(-1, 3.6) == -23.92


if __name__ == '__main__':
    test()
