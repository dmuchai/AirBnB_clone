#!/usr/bin/python3
"""Base model class with common functionality for other models."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines the Base Model class for the airbnb clone project"""
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel class instance"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)


    def __str__(self):
        """Prints representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self) 
        models.storage.save()

    def to_dict(self):
        """Convert instance attributes to dictionary format with ISO format"""
        serialized_obj = self.__dict__.copy()
        serialized_obj["__class__"] = self.__class__.__name__
        serialized_obj["created_at"] = self.created_at.isoformat()
        serialized_obj["updated_at"] = self.updated_at.isoformat()
        return serialized_obj


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
        print(
                f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}"
                )

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
