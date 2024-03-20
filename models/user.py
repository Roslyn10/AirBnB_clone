#!/usr/bin/python3
"""Defines a User class"""


class User(BaseModel):
    """
    A class representing a user.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    """

    email = ""
    password = ""
    first_name = ""
    last_namr = ""
