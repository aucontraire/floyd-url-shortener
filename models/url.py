#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel
import models
import os

class Url(BaseModel):
    '''
        Definition of the User class
    '''
    original = ''
    short_url = ''