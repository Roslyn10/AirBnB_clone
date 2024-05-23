#!/usr/python3
"""Defines unitessts for place.py"""

from models.base_model import BaseModel
import unittest
from models.place import Place

class test_Place(unittest.TestCare):
    """Tests for the class Place"""

    def Setup(self):
        """Set up test environment"""
        self.place = Place()

    def test_initial_attributes(self):
        """Test that initial attributes are correctly initialized"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.prie_by_night, 0)
        self.assertEqual(self.plae.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test that Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.place), BaseModel))
