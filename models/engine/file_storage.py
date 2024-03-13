#!/usr/bin/python3
import json
""" file storage file"""

class FileStorage:
    """ file stoage class linked to base model for storing files"""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def save(cls):
        """ serialises objects to json file"""
        serialised_objs = {}
        for key, obj in cls.__objects.items():
            serialised_objs[key] = obj.to_dict()

        with open(cls.__file_path, 'w') as file:
            json.dump(serialised_objs, file)
    
    @classmethod
    def load(cls):

        try:
            with open(cls.__file_path, 'r') as file:
                data = json.loadfile(file)
                for key, val in data.items:
                    class_name, obj_id = key.split('.')
                    cls.__objects[key] = globals()[classname](**val)
        except:
            FileNotFoundError
            pass

    @classmethod
    def reload(cls):
        cls.load()
        
    def all(cls):
        """Returns all objects from __objects."""
        return cls.__objects


    def get(cls, cls_name, obj_id):
        """Retrieves an object from __objects."""
        key = f"{cls_name}.{obj_id}"
        return cls.__objects.get(key)

    @classmethod
    def new(cls, obj):
        """Adds a new object to __objects."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        cls.__object[key] =  obj

