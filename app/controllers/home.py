from flask import Blueprint
from ..validators.home import HomeReponseSchema, HomeRequestSchema
from app.validators.api_validator import api_validator

controller_home = Blueprint('controller_home', __name__, url_prefix='/home')

@controller_home.get("")
@api_validator(resp=HomeReponseSchema)
def home():
    return {'msg': "*****Bem vindo****!"}, 200

@controller_home.post("/submit")
@api_validator(json=HomeRequestSchema)
def submit_home(data):
    try:
        return {'resp': f"Recebido: {data.user} e {data.password}"}, 200
    except Exception as e:
        return {'error': str(e)}, 500