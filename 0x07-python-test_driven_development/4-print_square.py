#!/usr/bin/python3
"""
This is print square module
"""


def print_square(size):
    """Print symbol #"""
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))