# Import libraries
from flask import Blueprint, jsonify

auth_router = Blueprint('auth', __name__)

# Routes
@auth_router.route('/login', methods = ['POST'])
def login():
  return jsonify({
    'message': 'token goes here'
  })

@auth_router.route('/register', methods = ['POST'])
def register():
  return jsonify({
    'message': 'token goes here'
  })