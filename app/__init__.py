from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .controllers import controller_home
    
    blueprints = [
        controller_home 
    ]
    
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    return app
