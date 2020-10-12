#!/usr/bin/python3
"""Module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size,size,x,y,id)

    def __str__(self):
        """ Special Method STR """
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return  st.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
