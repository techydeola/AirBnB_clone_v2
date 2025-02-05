#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import os
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer

try:
    from sqlalchemy.ext.declarative import declarative_base
except Exception:
    from sqlalchemy.orm import declarative_base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models """
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(
            String(60),
            primary_key=True,
            nullable=False,
            unique=True)
        
        created_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False)
        
        updated_at = Column(
            DateTime,
            default=datetime.utcnow(),
            nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            
            ca = 'created_at'
            ua = 'updated_at'
            if ca not in kwargs.keys() and ua not in kwargs.keys():
                self.created_at = self.updated_at = datetime.now()
            elif ca not in kwargs.keys():
                self.created_at = datetime.now()
            elif ua not in kwargs.keys():
                self.updated_at = datetime.now()
                
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
    
    def __repr__(self):
        """ This method return a string representation of the instance """
        
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        dictionary = dict(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        if '_sa_instance_state' in dictionary.keys():
            del dictionary["_sa_instance_state"]

        return dictionary
    
    def delete(self):
        """ This is a delete method that remove the current instance from the
        storage"""
        
        models.storage.delete(self)
