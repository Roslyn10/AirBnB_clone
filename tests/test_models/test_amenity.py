#!/usr/bin/python3
"""Defines unittests for amenity.py"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity

class test_Amenity(unittest.TestCare):
    """Tests for the class Amenity"""

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amentit()

    def test_initial_attributes(self):
        """Test that initial attributes are empty strings"""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test that Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))
