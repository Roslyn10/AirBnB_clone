#!/usr/bin/python3
"""Defines unittests for city.py"""

from models.base_model import BaseModel
import unittest
from models.city import City

class test_City(unittest.TestCare):
    """Tests for the class City"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def test_initial_attributes(self):
        """Test that initial attributes are empty strings"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test that City is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))
