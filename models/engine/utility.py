#!/usr/bin/python3
'''
    This module contains our helper functions for FileStorage and DBStorage.
'''
import models
import os

def convert_class(cls, choice="string"):
    '''
        This will convert our cls to a string in case it's not.
        Or it will return None.
    '''
    if choice == 'string':
        if cls is None or cls == "":
            c = None
        elif type(cls) != str:
            c = cls.__class__.__name__
        else:
            c = cls
        return c
    elif choice == 'class':
        c = convert_class(cls, 'string')
        return (models.classes.get(c))
