#!/usr/bin/python3
from models.rectangle import Rectangle
"""This module  has a Square class.
"""


class Square(Rectangle):

    """class Square.
    the class defines the private instance attributes:
    __width, __height, __x, __y

    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        my_attris = ["id", "size", "x", "y"]
        if args != None and args != ():
            for i in range(len(my_attris)):
                if i < len(args):
                    setattr(self, my_attris[i], args[i])
        elif kwargs != None and kwargs != {}:
            for key, value in kwargs.items():
                if key in my_attris:
                    setattr(self, key, value)

    def to_dictionary(self):
        new_dir = {}
        copy_dir = self.__dict__
        for k, v in self.__dict__.items():
            attr_sq = k.split("__")
            if len(attr_sq) > 1:
                if attr_sq[1] == "width" or attr_sq[1] == "height":
                    attr_sq[1] = "size"
                clear_attr = attr_sq[1]
            else:
                clear_attr = attr_sq[0]
            new_dir[clear_attr] = v
        return new_dir

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
