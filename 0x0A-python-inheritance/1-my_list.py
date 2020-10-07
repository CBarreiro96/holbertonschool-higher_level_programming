#!/bin/usr/python3
"""Class that inherits from list"""


class MyList(list):
    """"Classs my list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
