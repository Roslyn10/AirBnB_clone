#!/usr/bin/python3
"""Defines unittests for review.py"""

from models.base_model import BaseModel
import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """Tests for the class Review"""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def test_initial_attributes(self):
        """Test that initial attribbutes are empty strings"""
        self.assertEqual(self.review.place_is, "")
        self.assertEqual(self.review.user_is, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test that Review is a subclass off BaseModel"""
        self.assertTrue(issubclass(type(self.review), BaseModel))
