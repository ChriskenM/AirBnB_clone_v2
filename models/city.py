#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, string, ForeignKey 
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        __tablename__ (str): MySQL table to store Cities.
        name: The name of the City.
        state_id: The state id of the City.
    """
    __tablename__ = "cities"
    name = column(String(128), nullable=False)
    state_id = column(String(60), nullable=False, ForeignKey("states.id"))
