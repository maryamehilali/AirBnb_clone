#!/usr/bin/python3
"""module for the class FileStorage"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
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
            json.dump({key: value.to_dict() for key, value in
                       self.__objects.items()}, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        classes = ["Amenity", "BaseModel", "City",
                   "Place", "Review", "State", "User"]
        try:
            with open(self.__file_path, "r") as a_file:
                obj_dict = json.load(a_file)
                for p, worth in obj_dict.items():
                    class_name, obj_id = p.split('.')
                    if class_name in classes:
                        obj = eval(class_name)(**worth)
                        self.__objects[p] = obj

        except FileNotFoundError:
            pass
