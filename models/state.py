#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
            )
    else:
        @property
        def cities(self):
            """ returns list of City instances with state_id == to the current
            State.id """
            from models import storage
            cities = []
            for city in storage.all(City):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
