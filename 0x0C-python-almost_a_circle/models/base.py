#!/usr/bin/python3
import json
import os

"""This module  has a class.

The module has the class Base.
"""


class Base:

    """class Base.
    the class pass defines a id attribute.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None) or \
                (type(list_dictionaries) is not list) or \
                (len(list_dictionaries) == 0):

            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if (json_string is None) or \
                (type(json_string) is not str) or \
                (len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        my_dirS = []
        my_dirR = []
        a = 0
        b = 0
        if list_objs is None or \
                type(list_objs) is not list or len(list_objs) == 0:
            a = 2
        else:
            for obj in list_objs:
                if isinstance(obj, Base) is True and len(obj.__dict__) == 5:
                    a = 1
                    my_dirR.append(obj.to_dictionary())
                elif isinstance(obj, Base) is True and len(obj.__dict__) == 9:
                    b = 1
                    my_dirS.append(obj.to_dictionary())
        if a == 1 or a == 2:
            with open("Rectangle.json", mode="w", encoding="utf-8") as my_file:
                my_file.write(cls.to_json_string(my_dirR))
        if b == 1:
            with open("Square.json", mode="w", encoding="utf-8") as my_file2:
                my_file2.write(cls.to_json_string(my_dirS))

    @classmethod
    def create(cls, **dictionary):
        obj =cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        obj = cls(1, 1)
        if isinstance(obj, Base) is True and len(obj.__dict__) == 5:
            if os.path.isfile("Rectangle.json") is False:
                return []
            else:
                my_list = []
                with open("Rectangle.json", mode="r", encoding="utf-8") as my_file:
                    str_Rec = my_file.read()
                list_dicts = cls.from_json_string(str_Rec)
                for dic in list_dicts:
                    my_list.append(cls.create(**dic))
                return my_list
        elif isinstance(obj, Base) is True and len(obj.__dict__) == 9:
            if os.path.isfile("Square.json") is False:
                return []
            else:
                my_list = []
                with open("Square.json", mode="r", encoding="utf-8") as my_file:
                    str_Rec = my_file.read()
                list_dicts = cls.from_json_string(str_Rec)
                for dic in list_dicts:
                    my_list.append(cls.create(**dic))
                return my_list
        else:
            return []
