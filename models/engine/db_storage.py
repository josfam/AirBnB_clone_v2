#!/usr/bin/python3

"""This module defines a class to manage database storage for hbnb clone"""

import os
from sqlalchemy import create_engine, MetaData
from models.base_model import Base


class DBStorage:
    """Manages database storage for hbnb clone."""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB'),
            ),
            pool_pre_ping=True
        )
        # drop all tables if we are in test mode
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns all objects from the database if `cls` is not provided.
        Otherwise, objects matching `cls` are reurned.
        """
        all_objs = {}
        if cls is None:
            pass

    def new(self, obj):
        """Adds the provided object to the database."""
        pass

    def delete(self, obj=None):
        """Delete the provided object from the database,
        if `obj` is provided.
        """
        pass

    def save(self):
        """Commit all changes of the current database session."""
        pass

    def reload(self, obj=None):
        """Create all tables in the database, and creates the current database
        session from the engine.
        """
        pass
