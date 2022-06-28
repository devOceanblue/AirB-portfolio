from flasgger import swag_from
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.wishlist_service import WishlistService
from swaggers import wishlist_doc

wishlist_bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")


@wishlist_bp.route("", methods=["POST"])
@jwt_required()
@swag_from(wishlist_doc.wishlist_create)
def create_wishlist():
    """
    위시리스트 생성
    """
    data = request.get_json()
    current_user = get_jwt_identity()
    user_id = current_user.get("unique_id")

    wishlist_service = WishlistService()
    return wishlist_service.create_wishlist(user_id=user_id, body=data)


@wishlist_bp.route("/room", methods=["POST"])
@jwt_required()
@swag_from(wishlist_doc.wishlist_register)
def register_wishlist():
    data = request.get_json()

    wishlist_service = WishlistService()
    return wishlist_service.register_wishlist(body=data)


@wishlist_bp.route("/room/<id>", methods=["GET"])
@jwt_required()
@swag_from(wishlist_doc.wishlist_search)
def search_wishlist(id):
    wishlist_service = WishlistService()
    return wishlist_service.search_wishlist(id=id)


@wishlist_bp.route("/user", methods=["GET"])
@jwt_required()
@swag_from(wishlist_doc.wishlist_user_search)
def search_user_wishlist():
    """
    유저 위시리스트 목록 조회
    """
    current_user = get_jwt_identity()
    user_id = current_user.get("unique_id")
    wishlist_service = WishlistService()
    return make_response(jsonify(wishlist_service.search_user_wishlist(user_id)))


@wishlist_bp.route("/room/<id>", methods=["DELETE"])
@jwt_required()
@swag_from(wishlist_doc.wishlist_delete)
def delete_wishlist(id):
    wishlist_service = WishlistService()
    wishlist_service.delete_wishlist(id=id)
    return make_response("DELETED", 200)
