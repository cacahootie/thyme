import os

from flask import Flask, request, jsonify

basedir = os.path.dirname(os.path.abspath(__file__))

def get_instance(dbname=None, username=None, password=None, static_folder=None):
    app = Flask('thyme', static_folder=os.path.join(basedir,'static'))

    @app.route("/")
    def index():
        return app.send_static_file('index.html')

    return app
