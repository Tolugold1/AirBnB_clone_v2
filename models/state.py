#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel):
    """state class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """getter"""
            list_of_city = []
            for lt in models.storage.all(City).values():
                if City.State_id == self.id:
                    list_of_city.append(lt)
            return list_of_city
