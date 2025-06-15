from flask import jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.models import db

def register_restaurant_routes(app):
    
    @app.route('/restaurants/', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        results = [{
            'id': r.id,
            'name': r.name,
            'address': r.address
        } for r in restaurants]
        return jsonify(results), 200

    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': [{
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            } for rp in restaurant.restaurant_pizzas]
        }
        return jsonify(data), 200

    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404

        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
