#!/usr/bin/python3
"""Class square"""


class Square:
    """Class define a square by size and It can compute an area"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
