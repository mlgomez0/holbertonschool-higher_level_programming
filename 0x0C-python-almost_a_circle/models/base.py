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
        my_dirS = []
        my_dirR = []
        if list_objs == None:
            my_dir = []
        else:
            for obj in list_objs:
                if isinstance(obj, Base) is True and len(obj.__dict__) == 5:
                    my_dirR.append(obj.to_dictionary())
                elif isinstance(obj, Base) is True and len(obj.__dict__) == 9:
                    my_dirS.append(obj.to_dictionary())
            with open("Rectangle.json", mode="w", encoding="utf-8") as my_file1:
                my_file1.write(cls.to_json_string(my_dirR))
            with open("Square.json", mode="w", encoding="utf-8") as my_file2:
                my_file2.write(cls.to_json_string(my_dirS))
