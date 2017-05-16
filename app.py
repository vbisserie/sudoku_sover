# -*- coding: utf-8 -*-

from flask import Flask

from routes import index


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(index.blueprint)
    return _app


app = create_app()
