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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private instance height getter"""
        return self.__height

    @height.setter
    def height(self,value):
        """ Private instace height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """private instance x getter"""
        return self.__x

    @height.setter
    def x(self,value):
        """ Private instace x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """private instance y getter"""
        return self.__y

    @height.setter
    def y(self,value):
        """ Private instace y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.width * self.height
    
    def display(self):
        """prints in stdout the Rectangle 
        instance with the character #"""
        symbol = '#'
        if self.width == 0 and self.height == 0:
            return
        for j in range(self.height):
            print(symbol * self.width)
    
    def __str__(self):
        """ Special Method __str__ """
        Comment = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return Comment.format(self.id, self.x, self.y, self.width, self.height)