from typing import List

from commons.room import facilities
from data.Models.Model.room import facilities_map
from data.Models.address_repository import AddressRepository
from data.Models.room_repository import RoomRepository


class RoomService:
    def __init__(self):
        self.repo = RoomRepository()

    def _extract_dict_items(self, args, key):
        for k, v in dict(args[key]).items():
            args[k] = v
        del args[key]
        return args

    def _convert_arr_to_dict(self, arr, key):
        return dict(zip(facilities, arr))

    def _search_number_of_guests_id(self, number_of_guests):
        number_of_guest_id = self.repo.search_number_of_guest_id(number_of_guests)
        return number_of_guest_id

    def create(self, args: dict):
        # register address to db
        address_id = self.repo.register_address(args["address"])
        args["address"] = address_id

        image_urls = args.get("image_urls")
        del args["image_urls"]

        facilities_nums = list(map(int, args["facilities"].split(",")))
        args["facilities"] = [0] * len(facilities)
        for num in facilities_nums:
            args["facilities"][num] = 1

        facilities_dict = self._convert_arr_to_dict(args["facilities"], "facilities")
        args["facilities"] = facilities_dict
        args = self._extract_dict_items(args, "facilities")
        args = self._extract_dict_items(args, "number_info")
        args = self._extract_dict_items(args, "others")
        args["number_of_guests"] = args["number_of_guests"]

        result = self.repo.create(args)
        self.repo.register_filename(result, image_urls)
        return result

    def _categorize_fields(self, body):
        body["facilities"] = []

        facilities_dict = {
            "pool": 0,
            "jacuzzi": 1,
            "patio": 2,
            "barbecue_grill": 3,
            "firepit": 4,
            "billiard_table": 5,
            "indoor_fireplace": 6,
            "outdoor_dining_area": 7,
            "fitness_equipment": 8,
            "wifi": 9,
            "tv": 10,
            "kitchen": 11,
            "laundry_machine": 12,
            "free_parking_lot": 13,
            "air_conditioner": 14,
            "workspace": 15,
            "workspace": 16,
            "outdoor_shower_booth": 17,
            "first_aid_kit": 18,
            "carbon_monoxide_alarm": 19,
            "fire_extinguisher": 20,
        }
        # facilities
        for key, value in facilities_dict.items():
            if body[key]:
                body["facilities"].append(value)
            del body[key]

        body["others"] = {
            "security_camera": body["security_camera"],
            "weapon": body["weapon"],
            "dangerous_animal": body["dangerous_animal"],
        }
        del body["security_camera"]
        del body["weapon"]
        del body["dangerous_animal"]

        body["number_info"] = {
            "number_of_bathrooms": body["number_of_bathrooms"],
            "number_of_bedrooms": body["number_of_bedrooms"],
            "number_of_beds": body["number_of_beds"],
            "number_of_guests": body["number_of_guests"],
        }
        del body["number_of_bathrooms"]
        del body["number_of_bedrooms"]
        del body["number_of_beds"]
        del body["number_of_guests"]
        return body

    def get(self, id):
        address_repo = AddressRepository()

        room_info = self._categorize_fields(self.repo.get(id))
        address = address_repo.get(room_info["address"])

        room_info = {
            "address": {
                "address_name": address["address_name"],
                "b_code": address["b_code"],
                "h_code": address["h_code"],
                "main_address_no": address["main_address_no"],
                "mountain_yn": address["mountain_yn"],
                "region_1depth_name": address["region_1depth_name"],
                "region_2depth_name": address["region_2depth_name"],
                "region_3depth_h_name": address["region_3depth_h_name"],
                "region_3depth_name": address["region_3depth_name"],
                "sub_address_no": address["sub_address_no"],
                "x": address["x"],
                "y": address["y"],
            },
            "description": room_info["description"],
            "facilities": room_info["facilities"],
            "guest_area": room_info["guest_area"],
            "image_urls": room_info["image_urls"],
            "name": room_info["name"],
            "number_info": room_info["number_info"],
            "others": room_info["others"],
            "price": room_info["price"],
            "specialties": room_info["specialties"],
            "subtype": room_info["subtype"],
            "type": room_info["type"],
        }
        calendar = self.repo.get_calendar(id)
        review_info = self.repo.get_review_stats(id)
        return {
            "room": room_info,
            "reservation_calendar": calendar,
            "reviews": review_info,
        }

    def _get_number_info(
        self,
        body,
        number_of_guests,
        number_of_beds,
        number_of_bedrooms,
        number_of_bathrooms,
    ):
        body["number_info"] = [
            number_of_guests,
            number_of_beds,
            number_of_bedrooms,
            number_of_bathrooms,
        ]

    def _get_address(
        self,
        body,
        address_name,
        b_code,
        h_code,
        main_address_no,
        mountain_yn,
        region_1depth_name,
        region_2depth_name,
        region_3depth_h_name,
        region_3depth_name,
        road_region_1depth_name,
        road_region_2depth_name,
        road_region_3depth_name,
        sub_address_no,
        x,
        y,
    ):
        body['address'] = {
            'address_name': address_name,
            'b_code': b_code,
            'h_code': h_code,
            'main_address_no': main_address_no,
            'mountain_yn': mountain_yn,
            'region_1depth_name': region_1depth_name,
            'region_2depth_name': region_2depth_name,
            'region_3depth_h_name': region_3depth_name,
            'region_3depth_name': region_3depth_h_name,
            'road_region_1depth_name': road_region_1depth_name,
            'road_region_2depth_name': road_region_2depth_name,
            'road_region_3depth_name': road_region_3depth_name,
            'sub_address_no': sub_address_no,
            'x': x,
            'y': y,
        }

    def get_rooms_result_for_guest(
        self,
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

        kwargs = {
            "checkin": checkin,
            "checkout": checkout,
            "min_price": min_price,
            "max_price": max_price,
            "type": type,
            "number_of_guests": number_info[0],
            "number_of_beds": number_info[1],
            "number_of_bedrooms": number_info[2],
            "number_of_bathrooms": number_info[3],
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
        for f in facilities:
            kwargs[facilities_map[f]] = 1

        rows = self.repo.get_rooms_result_for_guest(**kwargs)
        result = []
        if rows:
            for rv in rows:

                result.append(rv)
        return result

    def make_reservation(
        self,
        room_id: int,
        checkin: str,
        checkout: str,
        price: int,
        number_of_guests: int,
        user_id: int,
    ):
        kwargs = {
            "room_id": room_id,
            "checkin": checkin,
            "checkout": checkout,
            "price": price,
            "number_of_guests": number_of_guests,
            "user_id": user_id,
        }

        self.repo.make_reservation(**kwargs)

    def close_room(self, body: dict = None):
        self.repo.close_room(body)

    def cancel_reservation(self, reservation_id):
        self.repo.cancel_reservation(reservation_id=reservation_id)

    def get_reservation_list(self, user_id, reservation_status):
        return self.repo.get_reservation_list(user_id, reservation_status)

    def change_reservation(self, reservation_id, body):
        self.repo.change_reservation(reservation_id, body)

    def host_search_reservation(self, user_id, reservation_status):
        return self.repo.host_search_reservation(
            user_id=user_id, reservation_status=reservation_status
        )
