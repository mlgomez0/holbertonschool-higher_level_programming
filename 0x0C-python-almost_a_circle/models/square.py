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
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y
        super().__init__(self.__width, self.__height, self.__x, self.__y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.__y, self.__width)

    def update(self, *args, **kwargs):
        m = 0
        if args != None and args != ():
            for arg in args:
                if m == 0:
                    self.id = arg
                if m == 1:
                    self.__width = arg
                    self.__height = arg
                if m == 2:
                    self.__x = arg
                if m == 3:
                    self.__y = arg
                m += 1
        elif kwargs != None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__width = value
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

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
        return self.__width

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value
