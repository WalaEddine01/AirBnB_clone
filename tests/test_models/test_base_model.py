#!/usr/bin/python3
"""
this module is for Unittesting BaseModel Class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import time


class TestBaseModel(unittest.TestCase):
    """
    This class to test BaseModel Class
    """
    def test_uuid(self):
        """Test that the id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_save(self):
        """
        Testing save method
        """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, model.created_at)


if __name__ == "__main__":
    unittest.main()
