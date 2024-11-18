#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up resources for tests."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up resources after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_instance_creation(self):
        """Test if storage is an instance of FileStorage."""
        self.assertIsInstance(self.storage, FileStorage)

    def test_new_and_save(self):
        """Test the new and save methods."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test the reload method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_all(self):
        """Test the all method."""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)


if __name__ == "__main__":
    unittest.main()
