#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private instance width getter"""
        return self.__width

    @width.setter
    def width(self,value):
        """ Private instace width setter"""
        self.__width = value

    @property
    def height(self):
        """Private instance height getter"""
        return self.__height

    @height.setter
    def height(self,value):
        """ Private instace height setter"""
        self.__height = value

    @property
    def x(self):
        """private instance x getter"""
        return self.__x

    @height.setter
    def x(self,value):
        """ Private instace x setter"""
        self.__x = value

    @property
    def y(self):
        """private instance y getter"""
        return self.__y

    @height.setter
    def y(self,value):
        """ Private instace y setter"""
        self.__y = value
