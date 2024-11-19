#!/usr/bin/python3
"""
Module that defines the FileStorage class.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    The Module for serialization-deserialization of data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
         Adds new object to __objects dict with key <obj class name>.id.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def save(self):
        """
        Serializes the __objects dict to the JSON format
        and saves it to the file specified by __file_path.
        """
        all_objs = self.__objects

        rep_dict = {}

        for obj in all_objs.keys():
            rep_dict[obj] = all_objs[obj].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(rep_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects dict,if it exists
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                try:
                    rep_dict = json.load(file)

                    for key, value in rep_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        self.__objects[key] = instance
                except Exception:
                    pass
