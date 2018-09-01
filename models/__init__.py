#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel
from models.url import Url
import os

classes = {"Url": Url, "BaseModel": BaseModel}


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()