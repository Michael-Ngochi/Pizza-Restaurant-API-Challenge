from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    restaurant_pizzas = relationship(
        "RestaurantPizza", 
        back_populates="restaurant", 
        cascade="all, delete"
    )
