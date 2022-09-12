#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.FileStorage import FileStorage
    storage = FileStorage()
storage.reload()
