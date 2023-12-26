# Import libraries
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Import the database and models
from database.models import db, User

auth_router = Blueprint('auth', __name__)

# Routes
@auth_router.route('/login', methods = ['POST'], endpoint = 'auth-login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username = username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity = user.id)
        return jsonify(access_token = access_token)
    else:
        return jsonify({ 'message': 'Invalid credentials' }), 401

@auth_router.route('/register', methods = ['POST'], endpoint = 'auth-register')
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the admin user exists or not
    admin_exists = User.query.filter_by(is_admin = True).first()

    new_user = User(username = username)
    new_user.set_password(password)

    # If not admin exists, create a new admin
    if not admin_exists:
        new_user.is_admin = True

    db.session.add(new_user)
    db.session.commit()

    # Login the new user after registration
    access_token = create_access_token(identity = new_user.id)

    if admin_exists:
        return jsonify({
            'message': 'User registered successfully (non-admin)',
            'access_token': access_token
        })
    else:
        return jsonify({
            'message': 'User registered successfully (admin)',
            'access_token': access_token
        })

@auth_router.route('/protected', methods = ['GET'], endpoint = 'auth-protected')
@jwt_required
def is_protected():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    return jsonify({ 'message': 'You are logged in', 'username': current_user.username })

@auth_router.route('/admin', methods = ['GET'], endpoint = 'auth-admin')
@jwt_required
def admin():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    if current_user.is_admin:
        return jsonify({ 'message': 'You are an admin' })
    else:
        return jsonify({ 'message': 'You are NOT an admin' }), 403
