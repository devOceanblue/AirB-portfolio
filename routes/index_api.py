from flask import Blueprint

index_bp = Blueprint("index", __name__, url_prefix="/")


@index_bp.route("")
def hello_world():  # put application's code here
    return "MainPage"
