#!/usr/bin/python3
""" Class students """


class Student:
    """class Student that defines a studen"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method json"""

        return self.__dict__.copy()
