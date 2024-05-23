#!/usr/bin/python3
"""Defines unittests for file_storage.py"""

import os
import unittest
from models.engine import
from models.base_model import BaseModel

class test_fileStorage(unittest.TestCase):
    """Class to test File Storage"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.id = "82949"
        self.base_model.name = "Test_model"
        self.storage.new(self.base_model)

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        storage = FileStorage()
        obj = storage.all()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel.82949", all_objects)

    def test_new(self):
        """Test that a new object is added to __objects"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIn("BaseModel.82949", self.storage.all())

    def test_save(self):
        """Test that save serializes objects to JSON file"""
        self.storage.save()
        with open("file.json", "r") as file:
            data = json.load(file)
        self.assertIn("BaseModel.82949", data)
        self.assertEqual(data["BaseModel.82949"]["name", "Test_model"))

    def test_reload(self):
        """Test that reload deserializes objects from JSOn file"""
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn("BaseModel.82949", all_objects)
        self.assertEqual(all_objects["BaseModel.82949"].name, "Test_model")

    def test_reload_no_file(self):
        """Test reload with no existing file"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_obj_list_empty(self):
        """Test that object is empty"""
        self.assertEqual(len(storage.all(), 0)

    def test_file_path(self):
    """Test that file_path is a string"""
    self.assertEqual(type(storage.all(),dict)
