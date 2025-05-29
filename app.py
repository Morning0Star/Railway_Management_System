from flask import Flask
from dotenv import load_dotenv
import logging
import os
from logging.config import dictConfig
from routes.auth import auth_bp
from routes.trains import trains_bp
from routes.bookings import bookings_bp
from middlewares.error_handler import handle_error
from config.database import init_db

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    init_db()
 
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(trains_bp, url_prefix='/api/v1/trains')
    app.register_blueprint(bookings_bp, url_prefix='/api/v1/bookings')

    app.register_error_handler(Exception, handle_error)
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False').lower() == 'true') 