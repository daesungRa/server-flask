import logging

from flask import Flask,Blueprint, jsonify

LOGGER = logging.getLogger(__name__)
API = Blueprint('main', __name__, url_prefix='/')


@API.route('/')
def flask_main():
    LOGGER.info('Call main!!')
    return jsonify(data='Hello Flask~!')

