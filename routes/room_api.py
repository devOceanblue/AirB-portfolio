import logging
from typing import List

from flasgger import swag_from
from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from commons.decorator.convert_params import convert_params
from commons.validator.room_validator import (
    guest_search_request,
    make_reservation_request,
)
from services.room_service import RoomService
from services.user_service import UserService
from swaggers import room_api_doc

room_bp = Blueprint("room", __name__, url_prefix="/room")


@room_bp.route("/host", methods=["POST"])
@jwt_required()
@swag_from(room_api_doc.room_register)
def create_room():
    """
    호스트 숙소 등록
    """
    result = None
    try:
        data = request.get_json()

        current_user = get_jwt_identity()

        from services.user_service import UserService

        user_service = UserService()
        user = user_service.search({"unique_id": current_user.get("unique_id")})

        user_service.patch(user["unique_id"], {"role": 2})
        data["user_id"] = user["unique_id"]
        room_service = RoomService()
        id = room_service.create(data)
        result = room_service.get(id=id)
        return make_response(jsonify(result))
    except Exception as e:
        logging.error(e)
        return make_response(jsonify(result))


@room_bp.route("/host", methods=["PATCH"])
@jwt_required()
@swag_from(room_api_doc.room_update)
def update_room():
    """
    호스트 숙소 정보 수정
    """


@room_bp.route("/host", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.room_search)
def search_room():
    """
    호스트 숙소 목록 조회
    """
    current_user = get_jwt_identity()
    room_service = RoomService()
    user_service = UserService()
    user = user_service.search(current_user)
    result = room_service.get({"user_id": user.get("unique_id")})
    return make_response(jsonify(result))


@room_bp.route("/host/reservation", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.host_search_reservation)
def host_search_reservation():
    """
    호스트 예약된 숙소 목록 조회
    """
    reservation_status = request.args.get("reservation_status")
    current_user = get_jwt_identity()
    user_id = current_user.get("unique_id")
    room_service = RoomService()
    result = room_service.host_search_reservation(
        user_id=user_id, reservation_status=reservation_status
    )
    return make_response(jsonify(result))


@room_bp.route("host/<room_id>", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.host_room_get)
def get_host_room(room_id):
    """
    호스트 숙소 id 검색
    """
    logging.getLogger().setLevel(logging.DEBUG)
    room_service = RoomService()
    result = room_service.get(room_id)
    return make_response(jsonify(result))


@room_bp.route("guest/<room_id>", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.guest_room_get)
def get_guest_room(room_id):
    """
    게스트 숙소 id 검색
    """
    logging.getLogger().setLevel(logging.DEBUG)
    room_service = RoomService()
    result = room_service.get(room_id)
    return make_response(jsonify(result))


@room_bp.route("/guest", methods=["GET"])
@convert_params(**guest_search_request)
@swag_from(room_api_doc.room_guest_search)
def guest_search(
    facilities: List[int] = None,
    checkin: str = None,
    checkout: str = None,
    min_price: int = None,
    max_price: int = None,
    type: int = None,
    number_info: List[int] = None,
    guest_area: int = None,
    host_language: str = None,
    superhost: bool = None,
    address_name: str = None,
    center_coordinate: List[float] = None,
    radius: float = None,
    region_1depth_name: str = None,
    region_2depth_name: str = None,
    region_3depth_name: str = None,
    h_code: int = None,
    b_code: int = None,
    main_address_no: int = None,
    sub_address_no: int = None,
    page: int = 1,
    per_page: int = 20,
):
    """
    게스트 숙소 검색
    """
    room_service = RoomService()

    kwargs = {
        "facilities": facilities,
        "checkin": checkin,
        "checkout": checkout,
        "min_price": min_price,
        "max_price": max_price,
        "type": type,
        "number_info": number_info,
        "guest_area": guest_area,
        "host_language": host_language,
        "superhost": superhost,
        "address_name": address_name,
        "center_coordinate": center_coordinate,
        "radius": radius,
        "region_1depth_name": region_1depth_name,
        "region_2depth_name": region_2depth_name,
        "region_3depth_name": region_3depth_name,
        "h_code": h_code,
        "b_code": b_code,
        "main_address_no": main_address_no,
        "sub_address_no": sub_address_no,
        "page": page,
        "per_page": per_page,
    }

    result = room_service.get_rooms_result_for_guest(**kwargs)
    return make_response(jsonify(result))


@room_bp.route("/guest/reservation", methods=["POST"])
@jwt_required()
@convert_params(**make_reservation_request)
@swag_from(room_api_doc.room_reservation)
def make_reservation(
    room_id: int, checkin: str, checkout: str, price: int, number_of_guests: int
):
    """
    숙소 예약
    """
    try:
        current_user = get_jwt_identity()
        user_id = current_user["unique_id"]

        kwargs = {
            "room_id": room_id,
            "checkin": checkin,
            "checkout": checkout,
            "price": price,
            "number_of_guests": number_of_guests,
            "user_id": user_id,
        }

        room_service = RoomService()
        room_service.make_reservation(**kwargs)
        return make_response("Succesfully reserved", 200)
    except:
        return make_response("reservation failed", 400)


@room_bp.route("host/close/<id>", methods=["POST"])
@jwt_required()
@swag_from(room_api_doc.room_close)
def close_room():
    """
    호스트가 달력탭에서 숙소 차단날짜(closed dates) 설정
    가격은 통일함
    """
    data = request.get_json()

    room_service = RoomService()
    result = room_service.close_room(data)
    return make_response(jsonify(result))


@room_bp.route("/guest/reservation/<reservation_id>", methods=["DELETE"])
@jwt_required()
@swag_from(room_api_doc.cancel_reservation)
def cancel_reservation(reservation_id):
    """
    게스트 예약 취소
    """
    room_service = RoomService()
    result = room_service.cancel_reservation(reservation_id=reservation_id)
    return make_response(jsonify(result))


@room_bp.route("/guest/reservation/<id>", methods=["PATCH"])
@jwt_required()
@swag_from(room_api_doc.change_reservation)
def change_reservation(id):
    """
    게스트 예약 변경(날짜나 숙박 인원 변경)
    """
    body = request.get_json()

    room_service = RoomService()
    result = room_service.change_reservation(id, body)
    return make_response(jsonify(result))


@room_bp.route("/guest/resevation", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.reservation_list)
def get_reservation_list():
    """
    게스트 예약 목록 조회
    """
    reservation_status = request.args.get("reservation_status")
    current_user = get_jwt_identity()
    user_id = current_user["unique_id"]
    room_service = RoomService()
    result = room_service.get_reservation_list(user_id, reservation_status)
    return make_response(jsonify(result))


@room_bp.route("/host/review/<id>", methods=["POST"])
@jwt_required()
@swag_from(room_api_doc.review_register)
def register_review(id):
    """
    숙소 리뷰 등록
    """
    return


@room_bp.route("/host/review/<review_id>", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.review_get)
def get_review(id):
    """
    숙소 리뷰 조회
    """
    return


@room_bp.route("/host/review/<review_id>/<user_id>", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.review_search)
def search_review(id):
    """
    숙소 리뷰 user_id 조회
    """
    return


@room_bp.route("/host/review/<id>", methods=["DELETE"])
@jwt_required()
@swag_from(room_api_doc.review_delete)
def delete_review(id):
    """
    숙소 리뷰 삭제
    """
    return


@room_bp.route("/host/review/<id>", methods=["PATCH"])
@jwt_required()
@swag_from(room_api_doc.review_update)
def update_review(id):
    """
    숙소 리뷰 수정
    """
    return


@room_bp.route("/guest/review/<id>", methods=["POST"])
@jwt_required()
@swag_from(room_api_doc.guest_review_register)
def register_guest_review(id):
    """
    게스트 리뷰 등록
    """
    return


@room_bp.route("/guest/review/<id>", methods=["GET"])
@jwt_required()
@swag_from(room_api_doc.guest_review_search)
def search_guest_review(id):
    """
    게스트 리뷰 조회
    """
    return


@room_bp.route("/guest/review/<id>", methods=["DELETE"])
@jwt_required()
@swag_from(room_api_doc.guest_review_delete)
def delete_guest_review(id):
    """
    게스트 리뷰 삭제
    """
    return


@room_bp.route("/guest/review/<id>", methods=["PATCH"])
@jwt_required()
@swag_from(room_api_doc.guest_review_update)
def update_guest_review(id):
    """
    게스트 리뷰 수정
    """
    return
