from flask import flask

from controllers import controller_home

def create_app():
    app = Flask(__name__)
       
    app.register_blueprint()