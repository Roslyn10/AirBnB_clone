#!/usr/bin/python3
"""Defines a Review class"""


class Review(BaseModel):
    """
    A class representing a review. 

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review text given by the user.

    """

    place_id = ""
    user_id = ""
    text = ""
