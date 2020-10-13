#!/usr/bin/python3
"""
Module Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
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
    def width(self, value):
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
    def height(self, value):
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
    def x(self, value):
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
    def y(self, value):
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
        print('\n' * self.y, end='')
        for row in range(self.height):
            print("{:s}{:s}".format(" "*self.x, "#"*self.width))

    def __str__(self):
        """ Special Method __str__ """
        Comment = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return Comment.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        Argument = ['id', 'width', 'height', 'x', 'y']
        Count = 0
        if args and len(args) != 0:
            for i in args:
                if Count == 0:
                    super().__init__(i)
                elif Count < len(Argument):
                    setattr(self, Argument[Count], i)
                Count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        Dict = {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
        return Dict
