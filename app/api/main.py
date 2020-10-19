import logging

from flask import Flask,Blueprint, jsonify

LOGGER = logging.getLogger(__name__)
API = Blueprint('main', __name__, url_prefix='/')


@API.route('test')
def test():
    LOGGER.info('Test call!!')
    return jsonify(data='Hello, Flask~!')

