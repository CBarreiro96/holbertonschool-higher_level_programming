#!/usr/bin/python3
"""Reads n lines of a text file (UTEF8)"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file
    (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        Lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(Lines):
            [print(i, end='') for i in Lines]
        else:
            [print(Lines[i], end='') for i in range(0, nb_lines)]
