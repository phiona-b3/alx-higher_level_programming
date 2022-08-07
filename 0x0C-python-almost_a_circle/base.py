#!/usr/bin/python3
"""Define Base class"""
import json
from os import path


class Base(object):
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialized constructor
        Args:
            id (int): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_distionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        with open(cls.__name__+'.json' , 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([0.to_dictionary() for o in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1,1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__+ '.json'
        if path.isfile(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                dictionary = cls.from_json_string(f.read())
            return[cls.create(**obj) for obj in dictionary]
        return []
