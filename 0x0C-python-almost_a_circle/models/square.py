#!/usr/bin/python3
"""Module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Special Method STR """
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return st.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Functions to update arguments  """
        Argumentlist = ["id", "size", "x", "y"]
        Count = 0
        if args and len(args) != 0:
            for ar in args:
                if Count == 0:
                    super().update(ar)
                elif Count < len(Argumentlist):
                    setattr(self, Argumentlist[Count], ar)
                Count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().update(id=value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dicitionary representation of Square """
        Dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return Dict
