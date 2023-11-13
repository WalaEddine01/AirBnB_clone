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
    '''
    def test_id(self):
        """Test that the id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
    '''
    def test_str(self):
        """
        To test the __str__ method
        """
        model = BaseModel()
        string = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(string, str(model))

    def test_save(self):
        """
        Testing save method
        """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_to_dict(self):
        """
        This method to test to_dict method
        """
        model = BaseModel()
        model.city = "batna"
        model.number = int(5)
        di = model.to_dict()
        self.assertIsInstance(di["created_at"], str)
        self.assertIsInstance(di["updated_at"], str)
        self.assertIsInstance(di["number"], int)
        self.assertEqual(di["number"], 5)
        self.assertEqual(di["city"], "batna")


if __name__ == "__main__":
    unittest.main()
