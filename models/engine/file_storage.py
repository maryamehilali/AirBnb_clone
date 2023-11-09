#!/usr/bin/python3
"""module for the class FileStorage"""
import json
from os.path import isfile


class FileStorage(object):
    """class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as a_file:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()}, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if isfile(self.__file_path):
            with open(self.__file_path, "r") as a_file:
                obj_dict = json.load(a_file)
                """not finished yet"""
