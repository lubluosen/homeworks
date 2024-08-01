from typing import Any
from flask import Blueprint
from flask import jsonify

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return jsonify(message="Hello, World!")


bp = Blueprint('contacts', __name__)


@bp.route('/contacts')
def contacts():
    return jsonify(message="Contacts app.")
