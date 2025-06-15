import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import app

# Seed data
with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create Pizzas (mix of common and localized)
    pizza1 = Pizza(name="Chicken Tikka", ingredients="Chicken Tikka, Mozzarella, Onions, Green Pepper")
    pizza2 = Pizza(name="Peri Peri Chicken", ingredients="Chicken, Peri Peri Sauce, Mozzarella, Sweet Corn")
    pizza3 = Pizza(name="BBQ Beef", ingredients="Beef, BBQ Sauce, Mozzarella, Onions")
    pizza4 = Pizza(name="Veggie Delight", ingredients="Mushrooms, Bell Peppers, Olives, Sweet Corn, Mozzarella")
    pizza5 = Pizza(name="Hawaiian", ingredients="Ham, Pineapple, Mozzarella")

    db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
    db.session.commit()

    # Create Restaurants (actual brands)
    restaurant1 = Restaurant(name="Pizza Inn", address="Westlands, Nairobi")
    restaurant2 = Restaurant(name="Pepino's Pizza", address="Moi Avenue, Nairobi")
    restaurant3 = Restaurant(name="Domino's Pizza", address="Galleria Mall, Nairobi")
    restaurant4 = Restaurant(name="Debonairs Pizza", address="Yaya Centre, Nairobi")
    restaurant5 = Restaurant(name="Pizza Mojo", address="Kilimani, Nairobi")

    db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
    db.session.commit()

    # Create RestaurantPizzas (Join records)
    rp1 = RestaurantPizza(price=12, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=restaurant1.id, pizza_id=pizza3.id)
    rp3 = RestaurantPizza(price=10, restaurant_id=restaurant2.id, pizza_id=pizza2.id)
    rp4 = RestaurantPizza(price=9, restaurant_id=restaurant3.id, pizza_id=pizza5.id)
    rp5 = RestaurantPizza(price=14, restaurant_id=restaurant4.id, pizza_id=pizza4.id)
    rp6 = RestaurantPizza(price=13, restaurant_id=restaurant5.id, pizza_id=pizza1.id)
    rp7 = RestaurantPizza(price=11, restaurant_id=restaurant5.id, pizza_id=pizza2.id)

    db.session.add_all([rp1, rp2, rp3, rp4, rp5, rp6, rp7])
    db.session.commit()

    print("Data inserted successfully!")
