from flask import Flask, make_response
from flask_cors import CORS
import logging
from routes import api_blueprints
from utils.email import mail
from flask_jwt_extended import (
    get_jwt,
    create_access_token,
    get_jwt_identity,
    set_access_cookies,
    JWTManager,
)
import os
from flasgger import Swagger
from datetime import datetime, timezone, timedelta
from utils.jwt import jwt_redis_blocklist
from config import DevelopmentConfig, ProductionConfig, StagingConfig
from test_config import TestConfig
from swaggers.templates import template
from sqlalchemy import create_engine

app = Flask(__name__)
app.register_blueprint(api_blueprints)

config = TestConfig
if os.getenv("WORK_ENV") == "PRODUCTION":
    config = ProductionConfig
elif os.getenv("WORK_ENV") == "STAGING":
    config = StagingConfig
elif os.getenv("WORK_ENV") == "DEVELOPMENT":
    config = DevelopmentConfig

app.config.from_object(config)
db_user = create_engine(
    app.config["USER_SQLALCHEMY_DATABASE_URI"], encoding="utf-8", max_overflow=0
)
db_room = create_engine(
    app.config["ROOM_SQLALCHEMY_DATABASE_URI"], encoding="utf-8", max_overflow=0
)

CORS(app)
mail.init_app(app)
jwt = JWTManager(app)
swagger = Swagger(app, template=template)


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return make_response("Bad Request", 400)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return make_response("NOT FOUND", 404)


@app.errorhandler(422)
def invalid_input(e):
    logging.error(e)
    return make_response("Invalid Input", 422)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return make_response("Internal Server Error, 500")


# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


# Callback function to check if a JWT exists in the redis blocklist
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


if __name__ == "__main__":
    app.run(host="0.0.0.0")
