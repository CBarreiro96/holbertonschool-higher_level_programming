#!/usr/bin/python3

""" Class that inherits from Rectangle """

Rectangle =__import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """constructor"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """method with square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
