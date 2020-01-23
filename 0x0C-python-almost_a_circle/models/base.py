#!/usr/bin/python3
"""This module  has a class for rectangule instances.

The module has the class Rectangle.
"""


class Base:

    """class rectangle.
    the class pass

    """

    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects = Base.__nb_objects
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
        pass
