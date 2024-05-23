#!/usr/bin/python3
"""Defines unittests for user.py"""

from models.base_model import BaseModel
import unittest
from models.user import User

class test_User(unittest.TestCare):
    """Tests for the class User"""

    def setUp(self):
        """Set up test methods"""
        self.user = User()

    def test_initial_attributes(self):
        """Test that initial attributes are empty strings"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_attributes(self):
        """Test settig attributes"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertequal(self.user.last_name, "Doe")

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel"""
        self.assertTrue(issubclass(type.user), BaseModel))
