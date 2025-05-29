from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from middlewares.validate import validate_with_schema
from schemas import UserSchema, LoginSchema
from controllers.auth_controller import register_user, login_user
from utils.errors import AuthenticationError

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@validate_with_schema(UserSchema)
def register():
    data = request.validated_data
    db = SessionLocal()
    try:
        register_user(db, data['email'], data['password'])
        return jsonify({"success": True, "message": "User registered"}), 201
    except AuthenticationError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@auth_bp.route('/login', methods=['POST'])
@validate_with_schema(LoginSchema)
def login():
    data = request.validated_data
    db = SessionLocal()
    try:
        token = login_user(db, data['email'], data['password'])
        return jsonify({"success": True, "token": token}), 200
    except AuthenticationError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close() 