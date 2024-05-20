#!/usr/bin/python3
"""Defines a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ A class representing a Place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The max number of guests allowed.
        price_by_night (int): The price per night.
        latitude (float): The latitude coordinates of the location
        longitude (float): The longitue coorfdinates of the location
        amentiy_ids (str): The  list of  Amenity id.

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
