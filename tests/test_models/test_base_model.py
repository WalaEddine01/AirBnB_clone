#!/usr/bin/python3
"""
this module is for Unittesting BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        """Test that the id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)


if __name__ == "__main__":
    unittest.main()

