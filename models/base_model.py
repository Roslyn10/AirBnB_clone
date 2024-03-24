#!/usr/bin/python3
"""Defines a Base Model for the AirBnB clone"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.name__,
                self.id,
                self.__dict__
        )

    def save(self):
        self.updated_at = datetime.now()
