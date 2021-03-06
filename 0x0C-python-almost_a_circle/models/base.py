#!/usr/bin/python3
"""Module base"""
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        jsonlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jsonlist.append(i.to_dictionary())
        DicJson = cls.to_json_string(jsonlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(DicJson)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        lists = []
        try:
            with open(filename, 'r') as file:
                lists = cls.from_json_string(file.read())
            for i, e in enumerate(lists):
                lists[i] = cls.create(**lists[i])
        except:
            pass
        return lists
