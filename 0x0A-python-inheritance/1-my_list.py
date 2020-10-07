#!/bin/usr/python3
"""Class that inherits from list"""


class MyList(list):
    """"prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
