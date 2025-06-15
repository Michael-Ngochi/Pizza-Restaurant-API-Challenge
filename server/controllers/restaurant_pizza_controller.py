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
            return jsonify({'error': 'Missing required fields'}), 400

        if price < 1 or price > 30:
            return jsonify({'error': 'Price must be between 1 and 30'}), 400

        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        response = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        return jsonify(response), 201
