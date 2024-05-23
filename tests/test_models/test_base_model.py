#!/usr/bin/python3
"""Defines unittests for base model.py"""

import os
import uuid import UUID
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    """Tests for the class BaseModel"""

    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()

    def test_id_is_unique(self):
        """Tests that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNoEqual(self.model.id, model2.id)

    def test_id_is_string(self):
        """Tests that is is a string"""
        self.assertIsInstance(slef.model.id, str)

    def test_created_at_is_datetime(self):
        """Tests that created_at is at datetime"""
        self.assertIsInstance(self.mode.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Tests that updated_at is at datetime"""
        self.assertIsInstance(self.mode.updated_at, datetime)

    def test_str_method(self):
        """Tests the __str__ method"""
        expected = (f"[BaseModel] ({self.model.id}) "
                    f"{self.model.__dict__}")
        self.assertEqual(str(self.model), expected)

    def test_save_method(self):
        """Tests the save method updates updated_at"""
        opd_update_at = self.model.updated_at
        self.model.save()
        self.assertNoEqual(self.model.updated_at, old_update_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Tests for the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
