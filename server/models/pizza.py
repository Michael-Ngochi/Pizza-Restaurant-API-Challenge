from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    restaurant_pizzas = relationship("RestaurantPizza", back_populates="pizza")
