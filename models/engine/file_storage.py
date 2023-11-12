#!/usr/bin/python3
"""
This module contains FileStorage class
"""
import json
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel


class FileStorage:
    """
    This class for serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the __objects dict
        """
        return FileStorage.__objects


    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj


    def save(self):
        """
        that serializes the data in __objects to our JSON file
        """
        jsn_file = {}
        for k, v in FileStorage.__objects.items():
            jsn_file[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(jsn_file, f)


    def reload(self):
        """
        that deserializes the data in our JSON file back
        to the dictionary __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                desr_file = json.load(f)
                for v in desr_file.values():
                    cls_n = v["__class__"]
                    if isinstance(cls_n, str) and type(eval(cls_n)) == type:
                        print(v["id"])
                        self.new(eval(cls_n)(**v))
        except FileNotFoundError:
            pass

