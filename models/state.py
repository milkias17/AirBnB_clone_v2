#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")

    @property
    def cities(self):
        """Getter for the cities attribute"""
        from models import storage
        cities = filter(lambda city: city.state_id ==
                        self.id, storage.all(City))
        return list(cities)
