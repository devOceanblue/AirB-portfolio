import logging
from datetime import timedelta

from flasgger import swag_from
from flask import (
    Blueprint,
    request,
    make_response,
    jsonify,
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_jwt,
)

from entities.user import User
from services.user_service import UserService
from swaggers import user_api_doc
from utils.jwt import jwt_redis_blocklist
from utils.token import confirm_verification_token

login_bp = Blueprint("user", __name__, url_prefix="/user")


@login_bp.route("/login", methods=["POST"])
@swag_from(user_api_doc.user_login)
def login():
    user_service = UserService()
    try:
        data = request.get_json()
        if data.get("id"):
            current_user = user_service.search({"id": data["id"]})
        if not current_user:
            return make_response("NOT FOUND", 404)
        current_user = dict(current_user)
        if current_user and not current_user.get("isVerified"):
            return make_response("Bad Request", 400)
        if user_service._verify_password(
            data["password"], current_user.get("password")
        ):
            access_token = create_access_token(
                identity={
                    "unique_id": current_user.get("unique_id"),
                    "id": current_user.get("id"),
                    "email": current_user.get("email"),
                }
            )
            refresh_token = create_refresh_token(
                identity={
                    "unique_id": current_user.get("unique_id"),
                    "id": current_user.get("id"),
                    "email": current_user.get("email"),
                }
            )
            resp = jsonify(
                {"access_token": access_token, "refresh_token": refresh_token}
            )
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp, 200
        else:
            return make_response("UNAUTHORIZED", 401)
    except Exception as e:
        logging.error(e)
        return make_response("Invalid Input", 422)


@login_bp.route("/logout", methods=["POST"])
@jwt_required()
@swag_from(user_api_doc.user_logout)
def logout():
    resp = jsonify({"msg": "succesfully logged out."})
    jti = get_jwt()["jti"]
    jwt_redis_blocklist.set(jti, "", ex=timedelta(hours=1))
    unset_jwt_cookies(resp)
    return resp


@login_bp.route("", methods=["POST"])
@swag_from(user_api_doc.user_register)
def register():
    user_service = UserService()
    try:
        data = request.get_json()
        if user_service.search({"id": data["id"]}):
            return make_response("Alreay registered.", 422)
        data["password"] = user_service._encrypt_password(data["password"])
        user = User(
            id=data.get("id"), password=data.get("password"), email=data.get("email"), role=data.get("role"), nickname=data.get("nickname"), description=data.get("description"), sex=data.get("sex")
        )
        user_service.create_user(user)
        return make_response(jsonify("registered"), 201)
    except Exception as e:
        logging.error(e)
        return make_response("Invalid Input", 422)


@login_bp.route("/confirm/<token>", methods=["GET"])
def verify_email(token):
    user_service = UserService()
    try:
        email = confirm_verification_token(token)
    except Exception as e:
        return make_response("SERVER_ERROR", 401)
    user = user_service.search({"email": email})
    if user.get("isVerified", None):
        return make_response("INVALID_INPUT", 422)
    else:
        user_service.patch(id=user.get("id", None), body={"isVerified": True})
        return make_response("E-mail verified, you can proceed to login now.", 200)


@login_bp.route("/refresh", methods=["GET"])
@jwt_required(refresh=True)
@swag_from(user_api_doc.user_refresh)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(
        identity={
            "unique_id": current_user.get("unique_id"),
            "id": current_user.get("id"),
            "email": current_user.get("email"),
        }
    )
    return jsonify(access_token=access_token)


@login_bp.route("/me", methods=["GET"])
@jwt_required()
@swag_from(user_api_doc.user_me)
def user_me_info():
    current_user = get_jwt_identity()
    user_id = current_user.get("unique_id")
    user_service = UserService()
    return jsonify(user_service.user_me_info(user_id))


@login_bp.route("/<id>", methods=["GET"])
@jwt_required()
@swag_from(user_api_doc.user_others)
def user_others_info(id):
    user_service = UserService()
    return jsonify(user_service.user_others_info(id))


@login_bp.route("/<id>", methods=["PATCH"])
@jwt_required()
@swag_from(user_api_doc.user_profile_update)
def user_profile_update(id):
    logging.getLogger().setLevel(logging.DEBUG)
    data = request.get_json()
    user_service = UserService()
    user_service.patch(id=id, body=data)
    return make_response("succefully updated", 200)
