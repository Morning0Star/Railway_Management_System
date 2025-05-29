from functools import wraps
from flask import request, jsonify
import jwt
import os
from utils.errors import AuthenticationError

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationError("Token is missing")
        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=["HS256"])
            request.user = data
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid token")
        except Exception:
            raise AuthenticationError("Invalid token")
    return decorated 