#!/bin/usr/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Class that define area and integer validator"""

    def area(self):
        """Exception that area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if(type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
