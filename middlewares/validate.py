from functools import wraps
from flask import request, jsonify
from marshmallow import Schema, ValidationError

def validate_with_schema(schema_class):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema = schema_class()
            try:
                if request.is_json:
                    data = schema.load(request.get_json())
                else:
                    data = schema.load(request.form)
                request.validated_data = data
                return f(*args, **kwargs)
            except ValidationError as err:
                formatted_errors = [
                    {"field": field, "message": ", ".join(messages)}
                    for field, messages in err.messages.items()
                ]
                return jsonify({
                    "error": "Validation failed",
                    "errors": formatted_errors
                }), 422
        return decorated_function
    return decorator 