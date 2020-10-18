from gevent import monkey
monkey.patch_all()

import logging
import os

from flask import Flask

from app.api import main

LOGGER = logging.getLogger(__name__)


def create_app() -> Flask:
    flask_app = Flask(__name__)
    register_blueprints(flask_app)
    flask_app.config['MAX_CONTENT_LENGTH'] = 1 << 40
    flask_app.secret_key = os.urandom(12)

    LOGGER.info('Setting done..')
    return flask_app


def register_blueprints(flask_app: Flask):
    flask_app.register_blueprint(main.API)
