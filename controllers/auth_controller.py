import bcrypt
import jwt
import os
from services.auth_service import find_user_by_email, create_user
from utils.errors import AuthenticationError

def register_user(db, email, password):
    if find_user_by_email(db, email):
        raise AuthenticationError("Email already registered")
    
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    return create_user(db, email, hashed.decode('utf-8'))

def login_user(db, email, password):
    user = find_user_by_email(db, email)
    if not user:
        raise AuthenticationError("Invalid credentials")
        
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        raise AuthenticationError("Invalid credentials")
        
    token = jwt.encode(
        {'id': user.id, 'role': user.role},
        os.getenv('JWT_SECRET'),
        algorithm='HS256'
    )
    
    return token 