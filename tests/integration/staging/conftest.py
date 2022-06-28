import pytest

from test_config import TestConfig
from flask import Flask
from flask_cors import CORS
from utils.email import mail
from flask_jwt_extended import (
    JWTManager,
)
from utils.jwt import JWT_Service


@pytest.fixture
def test_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    from app import api_blueprints

    app.register_blueprint(api_blueprints)
    CORS(app)
    mail.init_app(app)
    JWTManager(app)
    with app.app_context():
        yield app


@pytest.fixture
def test_cli(test_app):
    return test_app.test_client()


@pytest.fixture
def test_token(test_cli):
    access_token = JWT_Service.generate_access_token("4")
    refresh_token = JWT_Service.generate_refresh_token("4")
    yield {"access_token": access_token, "refresh_token": refresh_token}


@pytest.fixture
def test_header(test_token):
    headers = {"Authorization": f'Bearer {test_token["access_token"]}'}
    return headers
