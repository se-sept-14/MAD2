# Import libraries
import os
from flask import Flask
from flask_jwt_extended import JWTManager

# Import routes
from endpoints.auth import auth_router

# Import utilities and other stuff
from database.models import db

# Define a Flask instance
app = Flask(__name__)

# Configure an SQLite database
db_path = os.path.join(os.path.dirname(__file__), 'database', 'site.db')    # Use absolute path to store SQLite database in some other location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)      # Ideally, this should not be hardcoded and read from an environment file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'    # Ideally, this should again be read from an env file and NOT hardcoded here
jwt = JWTManager(app)

# Initialize the database
db.init_app(app)

# Register the router
app.register_blueprint(auth_router, url_prefix = '/api/auth')

# Create the tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)
