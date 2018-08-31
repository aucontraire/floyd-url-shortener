#!/usr/bin/python3
'''
    Package initializer
'''

from models.base_model import BaseModel, Base
from models.url import Url
import os

classes = {"Url": Url, "BaseModel": BaseModel}

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
