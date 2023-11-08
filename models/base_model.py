#!/usr/bin/python3
"""module for class BaseModel """
import uuid
import datetime


class BaseModel(object):
    """the class BaseModel that defines all common
    attributes/methods for other classes"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
