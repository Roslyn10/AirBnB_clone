#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city.

    Attributes:
        state_id (str): The id of a state.
        name (str): The name of the city.

    """

    state_id = ""
    name = ""
