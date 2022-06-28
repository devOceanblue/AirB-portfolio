from tests.integration.staging.conftest import test_cli, test_header

import pytest


class TestRoomCreate:
    def test_create_with_valid_parameters(self, test_cli, test_header):
        """
        호스트가 되기위해 숙소등록
        시작하기 버튼을 누르면
        숙소등록을 단계적으로 진행하는 화면의 API 구현
        숙소등록을 완료하면 User테이블의 사용자(User) 권한(role)을
        호스트(Host)로 변경하고, room 테이블에 숙소등록을 하고 status값을 PENDING(대기상태)로 만든다.
        room_images 테이블에 image url을 등록
        """

        params = {
            "type": 1,
            "subtype": 1,
            "guest_area": 1,
            "number_of_guests": 2,
            "number_of_beds": 2,
            "number_of_bedrooms": 2,
            "number_of_bathrooms": 2,
            "pool": 1,
            "jacuzzi": 1,
            "patio": 1,
            "barbecue_grill": 1,
            "firepit": 1,
            "billiard_table": 1,
            "indoor_fireplace": 1,
            "outdoor_dining_area": 1,
            "fitness_equipment": 1,
            "wifi": 1,
            "tv": 1,
            "kitchen": 1,
            "laundry_machine": 1,
            "free_parking_lot": 1,
            "pay_parking_lot": 1,
            "air_conditioner": 1,
            "workspace": 1,
            "outdoor_shower_booth": 1,
            "fire_alarm": 1,
            "first_aid_kit": 1,
            "carbon_monoxide_alarm": 1,
            "fire_extinguisher": 1,
            "security_camera": 1,
            "weapon": 1,
            "dangerous_animal": 1,
            "name": "jchangrom",
            "specialties": "xyz",
            "description": "abc",
            "price": 10000,
            "address": {
                "address_name": "전북 익산시 부송동 100",
                "y": "35.97664845766847",
                "x": "126.99597295767953",
                "address_name": "전북 익산시 부송동 100",
                "region_1depth_name": "전북",
                "region_2depth_name": "익산시",
                "region_3depth_name": "부송동",
                "region_3depth_h_name": "삼성동",
                "h_code": "4514069000",
                "b_code": "4514013400",
                "mountain_yn": "N",
                "main_address_no": "100",
                "sub_address_no": None,
                "road_address_name": "전북 익산시 망산길 11-17",
                "road_region_1depth_name": "전북",
                "road_region_2depth_name": "익산시",
                "road_region_3depth_name": "부송동",
                "road_name": "망산길",
                "underground_yn": "N",
                "road_main_building_no": "11",
                "road_sub_building_no": "17",
                "building_name": "",
                "zone_no": "54547",
            },
            "image_urls": ["a", "b", "c", "d", "e"],
        }
        resp = test_cli.post("/room", json=params, headers=test_header)
        assert resp.status_code == 200
        result = resp.json
        assert result
