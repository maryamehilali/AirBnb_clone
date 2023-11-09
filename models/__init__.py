#!/usr/bin/python3
"""module to create a unique FileStorage instance for the program"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
