from gevent import monkey
monkey.patch_all()

import logging
import os

from flask import Flask, render_template
from flask_cors import CORS

# import config  # TODO: Create default config file
from app.api import main

LOGGER = logging.getLogger(__name__)


def create_app() -> Flask:
    app = Flask(__name__)

    set_logger()
    register_blueprints(app)
    register_error_pages(app)
    app.config['MAX_CONTENT_LENGTH'] = 1 << 40
    app.config['SECRET_KEY'] = os.urandom(12)
    # app.config['PERMANENT_SESSION_LIFETIME'] = config.session_config['permanent_session_lifetime']
    
    CORS(app)

    LOGGER.info('Setting done..')
    return app


def set_logger():
    pass


def register_blueprints(app: Flask):
    app.register_blueprint(main.API)


def register_error_pages(app: Flask):
    @app.errorhandler(404)
    def page_not_found(error):
        LOGGER.error(error)
        return render_template('error/404.html'), 200


    @app.errorhandler(500)
    def server_side_error(error):
        LOGGER.error(error)
        return render_template('error/500.html'), 200

