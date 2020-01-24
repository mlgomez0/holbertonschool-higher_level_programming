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
