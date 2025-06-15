from flask import jsonify
from server.models.pizza import Pizza

def register_pizza_routes(app):
    
    @app.route('/pizzas/', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        results = [{
            'id': p.id,
            'name': p.name,
            'ingredients': p.ingredients
        } for p in pizzas]
        return jsonify(results), 200
