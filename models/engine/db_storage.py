#!/usr/bin/python3

"""This module defines a class to manage database storage for hbnb clone"""

import os
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User

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
        Otherwise, objects matching `cls` are returned.
        """

        matching_objs = {}
        session = self.__session

        if cls is None:
            table_classes = {State, City}
            for table_class in table_classes:
                table_rows = session.query(table_class)
                for table_row in table_rows:
                    plucked_info = {
                        '{}.{}'.format(
                            type(table_row).__name__, table_row.id): table_row
                    }
                    matching_objs.update(plucked_info)
        else:
            table_rows = session.query(cls)
            for table_row in table_rows:
                plucked_info = {
                    '{}.{}'.format(
                        type(table_row).__name__, table_row.id): table_row
                }
                matching_objs.update(plucked_info)
        return matching_objs

    def new(self, obj):
        """Adds the provided object to the database."""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Delete the provided object from the database,
        if `obj` is provided.
        """
        pass

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def reload(self):
        """Create all tables in the database, and creates the current database
        session from the engine.
        """
        engine = self.__engine
        Base.metadata.create_all(engine)

        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
