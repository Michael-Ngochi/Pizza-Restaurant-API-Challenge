from flask import jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models import db

def register_restaurant_pizza_routes(app):
    
     @app.route('/restaurant_pizzas/', methods=['POST'])
     def create_restaurant_pizza():
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not (price and pizza_id and restaurant_id):
            return jsonify({"errors": ["Missing required fields"]}), 400

        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        response = {
            "id": restaurant_pizza.id,
            "price": restaurant_pizza.price,
            "pizza_id": pizza.id,
            "restaurant_id": restaurant.id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }
        return jsonify(response), 201