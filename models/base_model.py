#!/usr/bin/python3
"""
This module defines the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initialize a new instance of the BaseModel class."""
        # Assign a unique id to the instance using uuid.uuid4()
        self.id = str(uuid.uuid4())
        # Assign the current datetime to the created_at and updated_at atributs
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        # Create a copy of the instance's __dict__ attribute
        d = self.__dict__.copy()
        # Add the class name to the dictionary under the key '__class__'
        d["__class__"] = self.__class__.__name__
        # Convert the created_at and updated_at attributes to ISO format strs
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
