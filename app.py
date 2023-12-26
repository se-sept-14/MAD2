# Import libraries
from flask import Flask

# Import routes
from endpoints.auth import auth_router

# Define a Flask instance
app = Flask(__name__)

# Register the router
app.register_blueprint(auth_router, url_prefix = '/api/auth')

if __name__ == '__main__':
  app.run(debug = True)
