import os
from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError, BaseModel
from werkzeug.exceptions import BadRequest

class ValidationException(BadRequest):
    def __init__(self, errors=None):
        super().__init__()
        self.errors = errors or []

def api_validator(json=None, resp=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if json is not None and request.method != 'GET':
                if request.is_json:
                    try:
                        data = json(**request.json)
                    except ValidationError as e:
                        raise ValidationException(errors=e.errors())
                else:
                    raise ValidationException(errors=[{"loc": ["body"], "msg": "Request data should be in JSON format", "type": "type_error"}])
                result = f(data, *args, **kwargs)
            else:
                result = f(*args, **kwargs)
            
            if resp is not None:
                if isinstance(result, tuple) and isinstance(result[0], dict):
                    response_data = result[0]
                    try:
                        resp(**response_data)
                    except ValidationError as e:
                        raise ValidationException(errors=e.errors())
                else:
                    raise ValidationException(errors=[{"loc": ["response"], "msg": "Controller function should return a tuple with a dictionary as the first element.", "type": "value_error"}])
            
            return jsonify(result[0]), result[1] if isinstance(result, tuple) else result
        return decorated_function
    return decorator
