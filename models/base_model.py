#!/usr/bin/python3
""" define a class Square """
from datetime import datetime
import uuid

class BaseModel:
	"""represents a base class"""

        def __init__(self, id: str, created_at: datetime, updated_at: datetime):
		""" initialise the base class 

                Args:
                    id (str): The unique identifier for the square.
                    created_at (datetime): The timestamp indicating when the square was created.
                    updated_at (datetime): The timestamp indicating when the square was last updated.
                """

		self.id = id
		self.created_at = created_at
		self.updated_at = updated_at
	
	def __str__(self, id)
                """Returns a string representation of the square."""
		return f'[self.name] (self.id) self.__dict__'
