from flask import Flask, jsonify
from .controllers.home import controller_home
from .validators.api_validator import ValidationException
from werkzeug.exceptions import BadRequest

def create_app():
    app = Flask(__name__)
    
    from .controllers import controller_home
    
    blueprints = [
        controller_home 
    ]
    
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    @app.errorhandler(ValidationException)
    def handle_validation_exception(error):
        response = {
            "errors": [
                {
                    "field": err.get("loc", ["unknown"])[-1],
                    "message": err.get("msg"),
                    "type": err.get("type")
                } for err in error.errors
            ]
        }
        return jsonify(response), error.code if isinstance(error, BadRequest) else 500
    
    return app
