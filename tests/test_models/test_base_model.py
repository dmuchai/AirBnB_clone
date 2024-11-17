#!/usr/bin/python3
"""Unittests for the BaseModel class."""
from datetime import datetime
import uuid
import os
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Unittests for the BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(uuid.UUID(model.id), uuid.UUID)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test __str__ representation."""
        model = BaseModel()
        string = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), string)

    def test_to_dict(self):
        """Test to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(
                model_dict["created_at"],
                model.created_at.isoformat()
                )
        self.assertEqual(
                model_dict["updated_at"],
                model.updated_at.isoformat()
                )

    def test_save(self):
        """Test save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)
        self.assertTrue(model.updated_at > old_updated_at)


if __name__ == "__main__":
    unittest.main()
