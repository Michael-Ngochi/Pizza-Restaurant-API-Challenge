from server.controllers.restaurant_controller import register_restaurant_routes
from server.controllers.pizza_controller import register_pizza_routes
from server.controllers.restaurant_pizza_controller import register_restaurant_pizza_routes

def register_routes(app):
    register_restaurant_routes(app)
    register_pizza_routes(app)
    register_restaurant_pizza_routes(app)
