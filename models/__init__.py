#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = None
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
elif storage_type == 'FileStorage':
    storage = FileStorage()

storage.reload()
