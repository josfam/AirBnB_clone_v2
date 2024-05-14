#!/usr/bin/python3

""" State Module for HBNB project """

from sqlalchemy import Table, Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = ...
