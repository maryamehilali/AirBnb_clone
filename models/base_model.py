#!/usr/bin/python3
"""module for class BaseModel """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation of the object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ This method updates the updated_at attribute with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/vlues
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
