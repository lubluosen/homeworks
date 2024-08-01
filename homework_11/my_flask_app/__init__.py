from flask import Flask
from flask import jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify(message='Hello, World!')

    @app.route('/contacts')
    def contacts():
        return jsonify(message='Contacts app.')

    return app
