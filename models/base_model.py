#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_2 = self.__dict__.copy()
        dict_2["__class__"] = __class__.__name__
        dict_2["created_at"] = self.__dict__["created_at"].isoformat()
        dict_2["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dict_2
