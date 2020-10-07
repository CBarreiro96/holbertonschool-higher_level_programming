#!/usr/bin/python3
"""Module for Square subclass."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area method through Super call """
        return super().area()

    def __str__(self):
        """ Method with square description """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
