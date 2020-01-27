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
        """__init__.

        init method to initiate every instance

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method to convert a list of dict into json string
        """
        if (list_dictionaries is None) or \
                (type(list_dictionaries) is not list) or \
                (len(list_dictionaries) == 0):

            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        method to convert a json string into a list
        of json string representations
        """
        if (json_string is None) or \
                (type(json_string) is not str) or \
                (len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes a json string representation
        into a file
        """
        class_name = cls.__name__
        file_name = class_name + ".json"
        my_dir = []
        a = 0
        if list_objs is not None and type(list_objs) == list:
            for obj in list_objs:
                if isinstance(obj, Base) is True:
                    a = 1
                    my_dir.append(obj.to_dictionary())
            if a == 1:
                with open(file_name, mode="w", encoding="utf-8") as my_file:
                    my_file.write(cls.to_json_string(my_dir))
        elif list_objs is None:
            with open(file_name, mode="w", encoding="utf-8") as my_file:
                my_file.write(str(my_dir))

    @classmethod
    def create(cls, **dictionary):
        """
        this method returns an instance with all elements
        already set
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        this method return a list of instances
        """
        class_name = cls.__name__
        my_file = class_name + ".json"
        if os.path.isfile(my_file) is False:
                return []
        else:
            my_list = []
            with open(my_file, mode="r", encoding="utf-8") as read_file:
                str_read = read_file.read()
            list_dicts = cls.from_json_string(str_read)
            for dic in list_dicts:
                my_list.append(cls.create(**dic))
            return my_list
