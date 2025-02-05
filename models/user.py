#!/usr/bin/python3
"""This module defines a class User"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import Place
        from models.review import Review
        
        __tablename__ = 'users'
        email = Column(
            String(128),
            nullable=False)
        
        password = Column(
            String(128),
            nullable=False)
        
        first_name = Column(
            String(128),
            nullable=True)
        
        last_name = Column(
            String(128),
            nullable=True)
        
        prices = relationship(
            "Place",
            backref="user",
            cascade="all, delete, delete-orphan")
        
        reviews = relationship(
            "Review",
            backref="user",
            cascade="all, delete, delete-orphan")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
