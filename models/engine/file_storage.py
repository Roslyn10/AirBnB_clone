#!/usr/bin/python3
"""Defines a class FileStorage"""
import json


class FileStorage:
    """A class that serializes instannces to a JSON file and deserializes JSOn file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        

    def save(self):
        """serializes __objects to the JSON file"""


    def reload(self):
        """deserializes the JSON file to __objects"""

    
