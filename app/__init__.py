from gevent import monkey
monkey.patch_all()

import logging
import os

from pathlib import Path
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
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

    LOGGER.info('Application setting done..')
    return app


def set_logger():
    fmt = Formatter(
        '[%(levelname)s %(asctime)s %(filename)s:%(lineno)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    root_logger = logging.getLogger()
    for handle in root_logger.handlers:
        root_logger.removeHandler(handle)

    # Add stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    stream_handler.setLevel(logging.INFO)
    root_logger.addHandler(stream_handler)

    # Add timed file handler
    project_root = Path(__file__).resolve().parent.parent
    log_dir = project_root / 'logs'
    log_dir.mkdir(exist_ok=True)
    file_handler = TimedRotatingFileHandler(
        filename=log_dir / 'app.log',
        when='midnight',
        interval=1,
        backupCount=100,
        encoding='UTF-8',
    )
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(logging.INFO)


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
