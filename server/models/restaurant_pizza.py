from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)

    restaurant = relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = relationship("Pizza", back_populates="restaurant_pizzas")

    __table_args__ = (
        CheckConstraint(price >= 1, name='price_min_check'),
        CheckConstraint(price <= 30, name='price_max_check'),
    )
