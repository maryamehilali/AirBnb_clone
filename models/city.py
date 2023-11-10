#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
