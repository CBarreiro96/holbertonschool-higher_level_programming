#!/usr/bin/python3
"""Module for Square subclass."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """
    def __init__(self, size):
        super().__init__(size, size)
