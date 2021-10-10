"""
Base application.
MAINTAINER: Ra Daesung (daesungra@gmail.com)
"""

import logging
from flask import render_template, jsonify

from apps.flasklib import ApiBlueprint


LOGGER = logging.getLogger(__name__)
API = ApiBlueprint(__name__, url_prefix='/')


@API.route('/')
def home():
    """
    Main page.

    TODO: Redirect login page if not logged in.
    """
    return render_template('index.html')


@API.route('/health')
def health():
    """
    Health check api.

    :return: message 'ok' with status code 200.
    """
    return jsonify(message='ok')
