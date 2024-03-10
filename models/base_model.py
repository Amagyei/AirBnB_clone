#!/usr/bin/python3
""" define a class Square """
import uuid

class Square:
	"""represents a base class"""

	def __init__(self, id, created_at, updated_at):
		""" initialise the base class """

		self.id = uuid.uuid1()
		self.created_at = created_at
		self.updated_at = updated_at
	
	def __str__(self, id)
		return f'[self.name] (self.id) self.__dict__'
