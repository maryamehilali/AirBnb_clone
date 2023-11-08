#!/usr/bin/python3
"""module for class BaseModel """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self):
        slef.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ This method updates the updated_at attribute with the current datetime. """
        self.updated_at = datetime.now()
