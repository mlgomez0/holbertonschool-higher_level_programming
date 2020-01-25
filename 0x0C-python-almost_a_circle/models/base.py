#!/usr/bin/python3
import json

"""This module  has a class.

The module has the class Base.
"""


class Base:

    """class Base.
    the class pass defines a id attribute.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects = Base.__nb_objects
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs == None:
            list_objs = []
        if issubclass(type(list_objs[0]), Base):
            with open("Rectangle.json", mode="w", encoding="utf-8") as my_file:
                my_json = cls.to_json_string(list_objs[0].to_dictionary())
                my_file.write(str(my_json))
        if issubclass(type(list_objs[0]), cls):
            with open("Square.json", mode="w", encoding ="utf-8") as my_file1:
                my_json = cls.to_json_string(list_objs[0].to_dictionary())
                my_file1.write(str(my_json))
