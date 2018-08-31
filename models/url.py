#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
import models
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Url(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "url"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        original = Column(String(225), nullable=False)
        short_url = Column(String(128), nullable=False)
    else:
        original = ''
        short_url = ''
