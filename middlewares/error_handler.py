from flask import jsonify

def handle_error(error):
    response = {
        "error": str(error),
        "message": getattr(error, 'description', str(error))
    }
    status_code = getattr(error, 'code', 500)
    return jsonify(response), status_code 