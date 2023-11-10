#!/usr/bin/python3
"""This moduale is contains a BaseModel Class"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel class
        """
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    obj_time = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, obj_time)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel class
        """
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the time
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        dict_2 = self.__dict__.copy()
        dict_2["__class__"] = __class__.__name__
        dict_2["created_at"] = self.__dict__["created_at"].isoformat()
        dict_2["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dict_2
