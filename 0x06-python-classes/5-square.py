#!/usr/bin/python3
"""
Class square with follow restriction
Default size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Methods of Area to find the size
Methods of print to pint #
"""


class Square:
    """A class that defines a square by size, which defaults 0.
    Square can also get area, and print square using '#'.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
