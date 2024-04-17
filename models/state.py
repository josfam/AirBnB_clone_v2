#!/usr/bin/python3
""" State Module for HBNB project """

import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """State class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        # State has a relationship with the class City, and all City objects
        # are deleted if their city is deleted
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan'
        )
    elif storage_type == 'FileStorage':
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the
            current State.id
            """
            from models import storage

            cities = storage.all('City')
            current_state_id = self.id

            return [
                city
                for city in cities.values()
                if city.state_id == current_state_id
            ]
