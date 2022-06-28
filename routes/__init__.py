from flask import Blueprint

from routes.index_api import index_bp
from routes.user_api import login_bp
from routes.room_api import room_bp
from routes.wishlist_api import wishlist_bp

groups = [index_bp, login_bp, room_bp, wishlist_bp]

api_blueprints = Blueprint("api_blueprints", __name__)
for bp in groups:
    api_blueprints.register_blueprint(bp)
