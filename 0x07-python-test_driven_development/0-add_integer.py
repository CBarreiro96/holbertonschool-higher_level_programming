#!/usr/bin/python3
"""
This is ADD integer module
"""


def add_integer(a, b=98):
    """Retrurn result of add the two number"""
    result = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(result):
        return int(a) + int(b)

    for x, y in list(zip(result, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
