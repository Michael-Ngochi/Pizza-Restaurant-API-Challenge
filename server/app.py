from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config
from server.controllers import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Register all routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
