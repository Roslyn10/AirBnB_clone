#!/usr/bin/python3
"""Defines  unittests for state.py"""

from models.base_model import BaseModel
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """Tests for the class State"""

    def setUp(self):
        """Set up test environments"""

    def test_initial_attributes(self):
        """Test that initial attributes are empty strings"""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))
