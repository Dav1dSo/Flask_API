from flask import Blueprint

controller_home = Blueprint('controller_home', __name__, url_prefix='/home')

@controller_home.get("/primeira-rota")
def home():
    return 'Página home!'