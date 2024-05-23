#!/usr/bin/python3
"""Defines a class FileStorage"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        self.classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                        "Place": Place, "Review": Review, "State": State, "User": User}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objdict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = self.classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
