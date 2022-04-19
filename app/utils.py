from functools import reduce


def fibonacci(number):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(number), [0, 1])[number]