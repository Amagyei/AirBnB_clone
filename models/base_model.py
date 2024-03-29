#!/usr/bin/python3

"""
This file defines  the BaseModel class which will.

serve as the base of ou model.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes."""

    def __init__(self, *args, **kwargs):
        """Deserialize and serialize a class."""
        """Initialize  if nothing is passed."""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            return

        """Using Key words (deserialize)."""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for Key, val in kwargs.items():
            if Key == "__class_":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        
        """Overide str representation of self."""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)


    def save(self):
        """updates the attribute aupdated_at"""
        self.updated_at = datetime.utcnow()
        return
