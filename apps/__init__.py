"""
My custom Flask web application.
MAINTAINER: Ra Daesung (daesungra@gmail.com)
"""

from gevent import monkey
monkey.patch_all()

import logging
import os

from pathlib import Path
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_cors import CORS

from .flasklib import NamuFlask
from .base.api.base import API as BASE_API

# from config import CONFIG  # TODO: Import CONFIG info if needed

LOGGER = logging.getLogger(__name__)


def create_app() -> Flask:
    app = NamuFlask(__name__)

    set_logger()
    register_blueprints(app)

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
        filename=log_dir / 'apps.log',
        when='midnight',
        interval=1,
        backupCount=100,
        encoding='UTF-8',
    )
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.CRITICAL)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(logging.ERROR)


def register_blueprints(app: Flask):
    app.register_blueprint(BASE_API)
