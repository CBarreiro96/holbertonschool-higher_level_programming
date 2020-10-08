#!/usr/bin/python3
""" Class students """


class Student:
    """ Class that defines a Student object """

    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        dic = self.__dict__.copy()
        return dic
