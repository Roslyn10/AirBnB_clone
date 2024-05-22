#!/usr/bin/python3
"""Defines a Base Model for the AirBnB clone"""

import uuid
#from models import storage
from datetime import datetime


class BaseModel:
    """
    A base class for all models in the AirBnB clone projet.

    Attributes:
        id (str): Unique identidier for each instance.
        created_at (datetime): The date and time when the instances created.
        updated_at (datetime): Date and time when the instance is last updated
        """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel

        Arguments:
            *args: Length of the argument list.
            **kwargs: Keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            #from models import storage
            #storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instances
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
        )

    def save(self):
        """
        Updates updated_at with the current date and time
        """
        self.updated_at = datetime.now()
        #from models import storage
        #storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance

        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
