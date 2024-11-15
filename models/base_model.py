#!/usr/bin/python3
"""Base model class with common functionality for other models."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines the Base Model class for the airbnb clone project"""
    def __init__(self):
        """Initialize the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance attributes to dictionary format with ISO format"""
        rep_dict = self.__dict__.copy()
        rep_dict["__class__"] = self.__class__.__name__
        rep_dict["created_at"] = self.created_at.isoformat()
        rep_dict["updated_at"] = self.updated_at.isoformat()
        return rep_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
