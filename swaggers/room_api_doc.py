room_register = {
    "tags": ["room/host"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소등록",
            "required": True,
            "schema": {"$ref": "#/definitions/Room_Create"},
        },
    ],
    "responses": {
        "200": {
            "description": "숙소 등록",
            "schema": {
                "type": "object",
                "properties": {
                    "room": {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "integer",
                                "description": "숙소 유형 1: 아파트 2:주택 3: 별채 4:독특한숙소 5: B&B 6:부티크호텔",
                            },
                            "subtype": {
                                "type": "integer",
                                "description": "숙소를 가장 잘 설명하는 문구 '1: 공동주택', '2: 공동주택(콘도)', '3: 로프트', '4: 레지던스', '5: 카사파르티쿨라르', '6: 휴가용주택', '7: 주거용공간', '8: 통나무집', '9: 저택', '10: 타운하우스', '11: 전원주택', '12: 방갈로', '13: 복토주택', '14: 하우스보트', '15: 오두막', '16: 농장체험숙소', '17: 돔하우스', '18: 키클라데스주택', '19: 샬레', '20: 담무소', '21: 등대', '22: 마차', '23: 초소형주택', '24: 트룰로', '25: 카사파르티쿨라르', '26: 펜션', '27: 휴가용주택', '28: 게스트용별채', '29: 게스트스위트', '30: 농장체험숙소', '31: 휴가용주택', '32: 헛간', '33: 보트', '34: 버스', '35: 캠핑카', '36: 트리하우스', '37: 캠핑장', '38: 성', '39: 동굴', '40: 돔하우스', '41: 복토주택', '42: 농장체험숙소', '43: 야영장', '44: 하우스보트', '45: 오두막', '46: 이글루', '47: 섬', '48: 등대', '49: 비행기', '50: 목장', '51: 종교건물', '52: 마차', '53: 화물컨테이너', '54: 텐트', '55: 초소형주택', '56: 티피', '57: 타워', '58: 기차', '59: 풍차', '60: 유르트', '61: 리아드', '62: 펜션', '63: 휴가용주택', '64: 기타', '65: B&B', '66: 산장', '67: 농장체험숙소', '68: 민수', '69: 카사파르티쿨라르', '70: 료칸', '71: 호텔', '72: 호스텔', '73: 리조트', '74: 산장', '75: 부티크호텔', '76: 아파트호텔', '77: 레지던스', '78: 헤리티지호텔', '79: 객잔' ",
                            },
                            "guest_area": {
                                "type": "integer",
                                "description": "게스트가 사용하는 공간범위(1:공간전체, 2:개인실, 3:다인실)",
                            },
                            "number_info": {
                                "type": "object",
                                "properties": {
                                    "number_of_beds": {
                                        "type": "integer",
                                    },
                                    "number_of_bedrooms": {
                                        "type": "integer",
                                    },
                                    "number_of_bathrooms": {
                                        "type": "integer",
                                    },
                                    "number_of_guests": {"type": "integer"},
                                },
                            },
                            "facilities": {
                                "type": "array",
                                "items": "integer",
                                "example": [15, 21],
                            },
                            "others": {
                                "type": "object",
                                "description": "기타 사항",
                                "properties": {
                                    "security_camera": {
                                        "type": "boolean",
                                    },
                                    "weapon": {
                                        "type": "boolean",
                                    },
                                    "dangerous_animal": {
                                        "type": "boolean",
                                    },
                                },
                            },
                            "name": {"type": "string", "example": "숙소 이름"},
                            "specialties": {
                                "type": "string",
                                "example": "숙소의 특징이 잘 드러나는 문구",
                            },
                            "description": {"type": "string", "example": "숙소 설명"},
                            "price": {"type": "integer", "description": "숙소 요금(1박기준)"},
                            "address": {
                                "type": "object",
                                "properties": {
                                    "address_name": {"type": "string"},
                                    "y": {"type": "number"},
                                    "x": {"type": "number"},
                                    "region_1depth_name": {"type": "string"},
                                    "region_2depth_name": {"type": "string"},
                                    "region_3depth_name": {"type": "string"},
                                    "region_3depth_h_name": {"type": "string"},
                                    "maintain_yn": {"type": "string"},
                                    "h_code": {"type": "integer"},
                                    "b_code": {"type": "integer"},
                                    "main_address_no": {"type": "integer"},
                                    "sub_address_no": {"type": "integer"},
                                },
                            },
                            "image_urls": {
                                "type": "array",
                                "items": "string",
                                "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                            },
                        },
                    },
                    "reservation_calendar": {"type": "array", "items": "object"},
                    "reviews": {"type": "array", "items": "object"},
                },
            },
        }
    },
    "definitions": {
        "Room_Create": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "integer",
                    "description": "숙소 유형 1: 아파트 2:주택 3: 별채 4:독특한숙소 5: B&B 6:부티크호텔",
                },
                "subtype": {
                    "type": "integer",
                    "description": "숙소를 가장 잘 설명하는 문구 '1: 공동주택', '2: 공동주택(콘도)', '3: 로프트', '4: 레지던스', '5: 카사파르티쿨라르', '6: 휴가용주택', '7: 주거용공간', '8: 통나무집', '9: 저택', '10: 타운하우스', '11: 전원주택', '12: 방갈로', '13: 복토주택', '14: 하우스보트', '15: 오두막', '16: 농장체험숙소', '17: 돔하우스', '18: 키클라데스주택', '19: 샬레', '20: 담무소', '21: 등대', '22: 마차', '23: 초소형주택', '24: 트룰로', '25: 카사파르티쿨라르', '26: 펜션', '27: 휴가용주택', '28: 게스트용별채', '29: 게스트스위트', '30: 농장체험숙소', '31: 휴가용주택', '32: 헛간', '33: 보트', '34: 버스', '35: 캠핑카', '36: 트리하우스', '37: 캠핑장', '38: 성', '39: 동굴', '40: 돔하우스', '41: 복토주택', '42: 농장체험숙소', '43: 야영장', '44: 하우스보트', '45: 오두막', '46: 이글루', '47: 섬', '48: 등대', '49: 비행기', '50: 목장', '51: 종교건물', '52: 마차', '53: 화물컨테이너', '54: 텐트', '55: 초소형주택', '56: 티피', '57: 타워', '58: 기차', '59: 풍차', '60: 유르트', '61: 리아드', '62: 펜션', '63: 휴가용주택', '64: 기타', '65: B&B', '66: 산장', '67: 농장체험숙소', '68: 민수', '69: 카사파르티쿨라르', '70: 료칸', '71: 호텔', '72: 호스텔', '73: 리조트', '74: 산장', '75: 부티크호텔', '76: 아파트호텔', '77: 레지던스', '78: 헤리티지호텔', '79: 객잔' ",
                },
                "guest_area": {
                    "type": "integer",
                    "description": "게스트가 사용하는 공간범위(1:공간전체, 2:개인실, 3:다인실)",
                },
                "number_info": {
                    "type": "object",
                    "properties": {
                        "number_of_beds": {
                            "type": "integer",
                        },
                        "number_of_bedrooms": {
                            "type": "integer",
                        },
                        "number_of_bathrooms": {
                            "type": "integer",
                        },
                        "number_of_guests": {
                            "type": "object",
                            "description": "adult:2, kid:1, infant:1, animal:0",
                            "properties": {
                                "adult": {"type": "integer"},
                                "kid": {"type": "integer"},
                                "infant": {"type": "integer"},
                                "animal": {"type": "integer"},
                            },
                        },
                    },
                },
                "facilities": {
                    "type": "array",
                    "items": "boolean",
                    "description": "편의시설",
                    "properties": {
                        "pool": {
                            "type": "boolean",
                        },
                        "jacuzzi": {
                            "type": "boolean",
                        },
                        "patio": {
                            "type": "boolean",
                        },
                        "barbecue_grill": {
                            "type": "boolean",
                        },
                        "firepit": {
                            "type": "boolean",
                        },
                        "billiard_table": {
                            "type": "boolean",
                        },
                        "indoor_fireplace": {
                            "type": "boolean",
                        },
                        "outdoor_dining_area": {
                            "type": "boolean",
                        },
                        "fitness_equipment": {
                            "type": "boolean",
                        },
                        "wifi": {
                            "type": "boolean",
                        },
                        "tv": {
                            "type": "boolean",
                        },
                        "kitchen": {
                            "type": "boolean",
                        },
                        "laundry_machine": {
                            "type": "boolean",
                        },
                        "free_parking_lot": {
                            "type": "boolean",
                        },
                        "air_conditioner": {
                            "type": "boolean",
                        },
                        "workspace": {
                            "type": "boolean",
                        },
                        "outdoor_shower_booth": {
                            "type": "boolean",
                        },
                        "fire_alarm": {
                            "type": "boolean",
                        },
                        "first_aid_kit": {
                            "type": "boolean",
                        },
                        "carbon_monoxide_alarm": {
                            "type": "boolean",
                        },
                        "fire_extinguisher": {
                            "type": "boolean",
                        },
                    },
                },
                "others": {
                    "type": "object",
                    "description": "기타 사항",
                    "properties": {
                        "security_camera": {
                            "type": "boolean",
                        },
                        "weapon": {
                            "type": "boolean",
                        },
                        "dangerous_animal": {
                            "type": "boolean",
                        },
                    },
                },
                "name": {"type": "string", "example": "숙소 이름"},
                "specialties": {"type": "string", "example": "숙소의 특징이 잘 드러나는 문구"},
                "description": {"type": "string", "example": "숙소 설명"},
                "price": {"type": "integer", "description": "숙소 요금(1박기준)"},
                "address": {
                    "type": "object",
                    "properties": {
                        "address_name": {"type": "string"},
                        "y": {"type": "number"},
                        "x": {"type": "number"},
                        "region_1depth_name": {"type": "string"},
                        "region_2depth_name": {"type": "string"},
                        "region_3depth_name": {"type": "string"},
                        "h_code": {"type": "integer"},
                        "b_code": {"type": "integer"},
                        "main_address_no": {"type": "integer"},
                        "sub_address_no": {"type": "integer"},
                        "country_id": {"type": "integer"},
                    },
                },
                "image_urls": {
                    "type": "array",
                    "items": "string",
                    "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                },
            },
        }
    },
}

room_update = {
    "tags": ["room/host"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소업데이트 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/Room_Update"},
        },
    ],
    "responses": {
        "200": {
            "description": "숙소 등록",
            "schema": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "integer",
                        "description": "숙소 유형 1: 아파트 2:주택 3: 별채 4:독특한숙소 5: B&B 6:부티크호텔",
                    },
                    "subtype": {
                        "type": "integer",
                        "description": "숙소를 가장 잘 설명하는 문구 '1: 공동주택', '2: 공동주택(콘도)', '3: 로프트', '4: 레지던스', '5: 카사파르티쿨라르', '6: 휴가용주택', '7: 주거용공간', '8: 통나무집', '9: 저택', '10: 타운하우스', '11: 전원주택', '12: 방갈로', '13: 복토주택', '14: 하우스보트', '15: 오두막', '16: 농장체험숙소', '17: 돔하우스', '18: 키클라데스주택', '19: 샬레', '20: 담무소', '21: 등대', '22: 마차', '23: 초소형주택', '24: 트룰로', '25: 카사파르티쿨라르', '26: 펜션', '27: 휴가용주택', '28: 게스트용별채', '29: 게스트스위트', '30: 농장체험숙소', '31: 휴가용주택', '32: 헛간', '33: 보트', '34: 버스', '35: 캠핑카', '36: 트리하우스', '37: 캠핑장', '38: 성', '39: 동굴', '40: 돔하우스', '41: 복토주택', '42: 농장체험숙소', '43: 야영장', '44: 하우스보트', '45: 오두막', '46: 이글루', '47: 섬', '48: 등대', '49: 비행기', '50: 목장', '51: 종교건물', '52: 마차', '53: 화물컨테이너', '54: 텐트', '55: 초소형주택', '56: 티피', '57: 타워', '58: 기차', '59: 풍차', '60: 유르트', '61: 리아드', '62: 펜션', '63: 휴가용주택', '64: 기타', '65: B&B', '66: 산장', '67: 농장체험숙소', '68: 민수', '69: 카사파르티쿨라르', '70: 료칸', '71: 호텔', '72: 호스텔', '73: 리조트', '74: 산장', '75: 부티크호텔', '76: 아파트호텔', '77: 레지던스', '78: 헤리티지호텔', '79: 객잔' ",
                    },
                    "guest_area": {
                        "type": "integer",
                        "description": "게스트가 사용하는 공간범위(1:공간전체, 2:개인실, 3:다인실)",
                    },
                    "number_info": {
                        "type": "object",
                        "properties": {
                            "number_of_beds": {
                                "type": "integer",
                            },
                            "number_of_bedrooms": {
                                "type": "integer",
                            },
                            "number_of_bathrooms": {
                                "type": "integer",
                            },
                            "number_of_guests": {
                                "type": "object",
                                "description": "adult:2, kid:1, infant:1, animal:0",
                                "properties": {
                                    "adult": {"type": "integer"},
                                    "kid": {"type": "integer"},
                                    "infant": {"type": "integer"},
                                    "animal": {"type": "integer"},
                                },
                            },
                        },
                    },
                    "facilities": {
                        "type": "object",
                        "description": "편의시설",
                        "properties": {
                            "pool": {
                                "type": "boolean",
                            },
                            "jacuzzi": {
                                "type": "boolean",
                            },
                            "patio": {
                                "type": "boolean",
                            },
                            "barbecue_grill": {
                                "type": "boolean",
                            },
                            "firepit": {
                                "type": "boolean",
                            },
                            "billiard_table": {
                                "type": "boolean",
                            },
                            "indoor_fireplace": {
                                "type": "boolean",
                            },
                            "outdoor_dining_area": {
                                "type": "boolean",
                            },
                            "fitness_equipment": {
                                "type": "boolean",
                            },
                            "wifi": {
                                "type": "boolean",
                            },
                            "tv": {
                                "type": "boolean",
                            },
                            "kitchen": {
                                "type": "boolean",
                            },
                            "laundry_machine": {
                                "type": "boolean",
                            },
                            "free_parking_lot": {
                                "type": "boolean",
                            },
                            "air_conditioner": {
                                "type": "boolean",
                            },
                            "workspace": {
                                "type": "boolean",
                            },
                            "outdoor_shower_booth": {
                                "type": "boolean",
                            },
                            "fire_alarm": {
                                "type": "boolean",
                            },
                            "first_aid_kit": {
                                "type": "boolean",
                            },
                            "carbon_monoxide_alarm": {
                                "type": "boolean",
                            },
                            "fire_extinguisher": {
                                "type": "boolean",
                            },
                        },
                    },
                    "others": {
                        "type": "object",
                        "description": "기타 사항",
                        "properties": {
                            "security_camera": {
                                "type": "boolean",
                            },
                            "weapon": {
                                "type": "boolean",
                            },
                            "dangerous_animal": {
                                "type": "boolean",
                            },
                        },
                    },
                    "name": {"type": "string", "example": "숙소 이름"},
                    "specialties": {"type": "string", "example": "숙소의 특징이 잘 드러나는 문구"},
                    "description": {"type": "string", "example": "숙소 설명"},
                    "price": {"type": "integer", "description": "숙소 요금(1박기준)"},
                    "address": {
                        "type": "object",
                        "properties": {
                            "address_name": {"type": "string"},
                            "y": {"type": "number"},
                            "x": {"type": "number"},
                            "region_1depth_name": {"type": "string"},
                            "region_2depth_name": {"type": "string"},
                            "region_3depth_name": {"type": "string"},
                            "h_code": {"type": "integer"},
                            "b_code": {"type": "integer"},
                            "main_address_no": {"type": "integer"},
                            "sub_address_no": {"type": "integer"},
                            "country_id": {"type": "integer"},
                        },
                    },
                    "image_urls": {
                        "type": "array",
                        "items": "string",
                        "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                    },
                },
            },
        }
    },
    "definitions": {
        "Room_Update": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "integer",
                    "description": "숙소 유형 1: 아파트 2:주택 3: 별채 4:독특한숙소 5: B&B 6:부티크호텔",
                },
                "subtype": {
                    "type": "integer",
                    "description": "숙소를 가장 잘 설명하는 문구 '1: 공동주택', '2: 공동주택(콘도)', '3: 로프트', '4: 레지던스', '5: 카사파르티쿨라르', '6: 휴가용주택', '7: 주거용공간', '8: 통나무집', '9: 저택', '10: 타운하우스', '11: 전원주택', '12: 방갈로', '13: 복토주택', '14: 하우스보트', '15: 오두막', '16: 농장체험숙소', '17: 돔하우스', '18: 키클라데스주택', '19: 샬레', '20: 담무소', '21: 등대', '22: 마차', '23: 초소형주택', '24: 트룰로', '25: 카사파르티쿨라르', '26: 펜션', '27: 휴가용주택', '28: 게스트용별채', '29: 게스트스위트', '30: 농장체험숙소', '31: 휴가용주택', '32: 헛간', '33: 보트', '34: 버스', '35: 캠핑카', '36: 트리하우스', '37: 캠핑장', '38: 성', '39: 동굴', '40: 돔하우스', '41: 복토주택', '42: 농장체험숙소', '43: 야영장', '44: 하우스보트', '45: 오두막', '46: 이글루', '47: 섬', '48: 등대', '49: 비행기', '50: 목장', '51: 종교건물', '52: 마차', '53: 화물컨테이너', '54: 텐트', '55: 초소형주택', '56: 티피', '57: 타워', '58: 기차', '59: 풍차', '60: 유르트', '61: 리아드', '62: 펜션', '63: 휴가용주택', '64: 기타', '65: B&B', '66: 산장', '67: 농장체험숙소', '68: 민수', '69: 카사파르티쿨라르', '70: 료칸', '71: 호텔', '72: 호스텔', '73: 리조트', '74: 산장', '75: 부티크호텔', '76: 아파트호텔', '77: 레지던스', '78: 헤리티지호텔', '79: 객잔' ",
                },
                "guest_area": {
                    "type": "integer",
                    "description": "게스트가 사용하는 공간범위(1:공간전체, 2:개인실, 3:다인실)",
                },
                "number_info": {
                    "type": "object",
                    "properties": {
                        "number_of_beds": {
                            "type": "integer",
                        },
                        "number_of_bedrooms": {
                            "type": "integer",
                        },
                        "number_of_bathrooms": {
                            "type": "integer",
                        },
                        "number_of_guests": {
                            "type": "object",
                            "description": "adult:2, kid:1, infant:1, animal:0",
                            "properties": {
                                "adult": {"type": "integer"},
                                "kid": {"type": "integer"},
                                "infant": {"type": "integer"},
                                "animal": {"type": "integer"},
                            },
                        },
                    },
                },
                "facilities": {
                    "type": "object",
                    "description": "편의시설",
                    "properties": {
                        "pool": {
                            "type": "boolean",
                        },
                        "jacuzzi": {
                            "type": "boolean",
                        },
                        "patio": {
                            "type": "boolean",
                        },
                        "barbecue_grill": {
                            "type": "boolean",
                        },
                        "firepit": {
                            "type": "boolean",
                        },
                        "billiard_table": {
                            "type": "boolean",
                        },
                        "indoor_fireplace": {
                            "type": "boolean",
                        },
                        "outdoor_dining_area": {
                            "type": "boolean",
                        },
                        "fitness_equipment": {
                            "type": "boolean",
                        },
                        "wifi": {
                            "type": "boolean",
                        },
                        "tv": {
                            "type": "boolean",
                        },
                        "kitchen": {
                            "type": "boolean",
                        },
                        "laundry_machine": {
                            "type": "boolean",
                        },
                        "free_parking_lot": {
                            "type": "boolean",
                        },
                        "air_conditioner": {
                            "type": "boolean",
                        },
                        "workspace": {
                            "type": "boolean",
                        },
                        "outdoor_shower_booth": {
                            "type": "boolean",
                        },
                        "fire_alarm": {
                            "type": "boolean",
                        },
                        "first_aid_kit": {
                            "type": "boolean",
                        },
                        "carbon_monoxide_alarm": {
                            "type": "boolean",
                        },
                        "fire_extinguisher": {
                            "type": "boolean",
                        },
                    },
                },
                "others": {
                    "type": "object",
                    "description": "기타 사항",
                    "properties": {
                        "security_camera": {
                            "type": "boolean",
                        },
                        "weapon": {
                            "type": "boolean",
                        },
                        "dangerous_animal": {
                            "type": "boolean",
                        },
                    },
                },
                "name": {"type": "string", "example": "숙소 이름"},
                "specialties": {"type": "string", "example": "숙소의 특징이 잘 드러나는 문구"},
                "description": {"type": "string", "example": "숙소 설명"},
                "price": {"type": "integer", "description": "숙소 요금(1박기준)"},
                "address": {
                    "type": "object",
                    "properties": {
                        "address_name": {"type": "string"},
                        "y": {"type": "number"},
                        "x": {"type": "number"},
                        "region_1depth_name": {"type": "string"},
                        "region_2depth_name": {"type": "string"},
                        "region_3depth_name": {"type": "string"},
                        "h_code": {"type": "integer"},
                        "b_code": {"type": "integer"},
                        "main_address_no": {"type": "integer"},
                        "sub_address_no": {"type": "integer"},
                        "country_id": {"type": "integer"},
                    },
                },
                "image_urls": {
                    "type": "array",
                    "items": "string",
                    "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                },
            },
        }
    },
}


room_search = {
    "tags": ["room/host"],
    "description": "숙소관리 - 숙소탭 숙소목록 조회",
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "query",
            "name": "number_of_beds",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "query",
            "name": "number_of_bedrooms",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "query",
            "name": "number_of_bathrooms",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "query",
            "name": "number_of_beds",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "숙소 id",
                    },
                    "number_of_beds": {
                        "type": "integer",
                    },
                    "number_of_bedrooms": {
                        "type": "integer",
                    },
                    "number_of_bathrooms": {
                        "type": "integer",
                    },
                    "name": {
                        "type": "string",
                    },
                    "country_id": {
                        "type": "integer",
                    },
                    "address": {
                        "type": "integer",
                    },
                    "status": {
                        "type": "integer",
                    },
                    "guest_area": {"type": "string"},
                    "updated_at": {"type": "string"},
                },
            },
        }
    },
}


host_room_get = {
    "tags": ["room/host"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "room_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "숙소 id",
                    },
                    "type": {
                        "type": "string",
                        "description": "숙소 유형",
                    },
                    "subtype": {
                        "type": "string",
                        "description": "숙소를 가장 잘 설명하는 문구",
                    },
                    "guest_area": {
                        "type": "string",
                        "description": "게스트가 사용하는 공간범위",
                    },
                    "number_of_guests": {
                        "type": "object",
                        "description": "adult:2, kid:1, infant:1, animal:0",
                        "properties": {
                            "adult": {"type": "integer"},
                            "kid": {"type": "integer"},
                            "infant": {"type": "integer"},
                            "animal": {"type": "integer"},
                        },
                    },
                    "facilities": {
                        "type": "object",
                        "description": "편의시설",
                        "properties": {
                            "pool": {
                                "type": "boolean",
                            },
                            "jacuzzi": {
                                "type": "boolean",
                            },
                            "patio": {
                                "type": "boolean",
                            },
                            "barbecue_grill": {
                                "type": "boolean",
                            },
                            "firepit": {
                                "type": "boolean",
                            },
                            "billiard_table": {
                                "type": "boolean",
                            },
                            "indoor_fireplace": {
                                "type": "boolean",
                            },
                            "outdoor_dining_area": {
                                "type": "boolean",
                            },
                            "fitness_equipment": {
                                "type": "boolean",
                            },
                            "wifi": {
                                "type": "boolean",
                            },
                            "tv": {
                                "type": "boolean",
                            },
                            "kitchen": {
                                "type": "boolean",
                            },
                            "laundry_machine": {
                                "type": "boolean",
                            },
                            "free_parking_lot": {
                                "type": "boolean",
                            },
                            "air_conditioner": {
                                "type": "boolean",
                            },
                            "workspace": {
                                "type": "boolean",
                            },
                            "outdoor_shower_booth": {
                                "type": "boolean",
                            },
                            "fire_alarm": {
                                "type": "boolean",
                            },
                            "first_aid_kit": {
                                "type": "boolean",
                            },
                            "carbon_monoxide_alarm": {
                                "type": "boolean",
                            },
                            "fire_extinguisher": {
                                "type": "boolean",
                            },
                        },
                    },
                    "number_of_beds": {
                        "type": "integer",
                    },
                    "number_of_bedrooms": {
                        "type": "integer",
                    },
                    "number_of_bathrooms": {
                        "type": "integer",
                    },
                    "name": {
                        "type": "string",
                    },
                    "specialties": {
                        "type": "string",
                    },
                    "description": {
                        "type": "string",
                    },
                    "price": {
                        "type": "integer",
                    },
                    "others": {
                        "type": "object",
                        "description": "기타 사항",
                        "properties": {
                            "security_camera": {
                                "type": "boolean",
                            },
                            "weapon": {
                                "type": "boolean",
                            },
                            "dangerous_animal": {
                                "type": "boolean",
                            },
                        },
                    },
                    "country_id": {
                        "type": "integer",
                    },
                    "city_id": {
                        "type": "integer",
                    },
                    "state_id": {
                        "type": "integer",
                    },
                    "address": {
                        "type": "integer",
                    },
                    "status": {
                        "type": "integer",
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "호스트 id",
                    },
                    "x": {
                        "type": "number",
                    },
                    "y": {
                        "type": "number",
                    },
                    "iron": {
                        "type": "boolean",
                    },
                    "breakfast": {
                        "type": "boolean",
                    },
                    "reviews": {
                        "type": "array",
                        "items": {
                            "properties": {
                                "nickname": {"type": "string", "description": "유저 닉네임"},
                                "message": {"type": "string", "description": "리뷰 내용"},
                                "created_at": {
                                    "type": "string",
                                    "description": "후기 남긴 날짜",
                                },
                            },
                        },
                        "description": "숙소 리뷰 목록",
                    },
                    "review_point": {"type": "object", "description": "숙소 리뷰 평점"},
                    "review_count": {"type": "integer", "description": "리뷰수 "},
                    "reservation_calendar": {
                        "type": "array",
                        "items": "string",
                        "description": "예약 가능한 날짜 보여주는 캘린더",
                        "example": ["2022-01-01", "2022-01-02"],
                    },
                    "image_urls": {
                        "type": "array",
                        "items": "string",
                        "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                    },
                },
            },
        }
    },
}


guest_room_get = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "room_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "숙소 id",
                    },
                    "type": {
                        "type": "string",
                        "description": "숙소 유형",
                    },
                    "subtype": {
                        "type": "string",
                        "description": "숙소를 가장 잘 설명하는 문구",
                    },
                    "guest_area": {
                        "type": "string",
                        "description": "게스트가 사용하는 공간범위",
                    },
                    "number_of_guests": {
                        "type": "object",
                        "description": "adult:2, kid:1, infant:1, animal:0",
                        "properties": {
                            "adult": {"type": "integer"},
                            "kid": {"type": "integer"},
                            "infant": {"type": "integer"},
                            "animal": {"type": "integer"},
                        },
                    },
                    "facilities": {
                        "type": "object",
                        "description": "편의시설",
                        "properties": {
                            "pool": {
                                "type": "boolean",
                            },
                            "jacuzzi": {
                                "type": "boolean",
                            },
                            "patio": {
                                "type": "boolean",
                            },
                            "barbecue_grill": {
                                "type": "boolean",
                            },
                            "firepit": {
                                "type": "boolean",
                            },
                            "billiard_table": {
                                "type": "boolean",
                            },
                            "indoor_fireplace": {
                                "type": "boolean",
                            },
                            "outdoor_dining_area": {
                                "type": "boolean",
                            },
                            "fitness_equipment": {
                                "type": "boolean",
                            },
                            "wifi": {
                                "type": "boolean",
                            },
                            "tv": {
                                "type": "boolean",
                            },
                            "kitchen": {
                                "type": "boolean",
                            },
                            "laundry_machine": {
                                "type": "boolean",
                            },
                            "free_parking_lot": {
                                "type": "boolean",
                            },
                            "air_conditioner": {
                                "type": "boolean",
                            },
                            "workspace": {
                                "type": "boolean",
                            },
                            "outdoor_shower_booth": {
                                "type": "boolean",
                            },
                            "fire_alarm": {
                                "type": "boolean",
                            },
                            "first_aid_kit": {
                                "type": "boolean",
                            },
                            "carbon_monoxide_alarm": {
                                "type": "boolean",
                            },
                            "fire_extinguisher": {
                                "type": "boolean",
                            },
                        },
                    },
                    "number_of_beds": {
                        "type": "integer",
                    },
                    "number_of_bedrooms": {
                        "type": "integer",
                    },
                    "number_of_bathrooms": {
                        "type": "integer",
                    },
                    "name": {
                        "type": "string",
                    },
                    "specialties": {
                        "type": "string",
                    },
                    "description": {
                        "type": "string",
                    },
                    "price": {
                        "type": "integer",
                    },
                    "others": {
                        "type": "object",
                        "description": "기타 사항",
                        "properties": {
                            "security_camera": {
                                "type": "boolean",
                            },
                            "weapon": {
                                "type": "boolean",
                            },
                            "dangerous_animal": {
                                "type": "boolean",
                            },
                        },
                    },
                    "country_id": {
                        "type": "integer",
                    },
                    "city_id": {
                        "type": "integer",
                    },
                    "state_id": {
                        "type": "integer",
                    },
                    "address": {
                        "type": "integer",
                    },
                    "status": {
                        "type": "integer",
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "호스트 id",
                    },
                    "x": {
                        "type": "number",
                    },
                    "y": {
                        "type": "number",
                    },
                    "iron": {
                        "type": "boolean",
                    },
                    "breakfast": {
                        "type": "boolean",
                    },
                    "reviews": {
                        "type": "array",
                        "items": {
                            "properties": {
                                "nickname": {"type": "string", "description": "유저 닉네임"},
                                "message": {"type": "string", "description": "리뷰 내용"},
                                "created_at": {
                                    "type": "string",
                                    "description": "후기 남긴 날짜",
                                },
                            },
                        },
                        "description": "숙소 리뷰 목록",
                    },
                    "review_point": {"type": "object", "description": "숙소 리뷰 평점"},
                    "review_count": {"type": "integer", "description": "리뷰수 "},
                    "reservation_calendar": {
                        "type": "array",
                        "items": "string",
                        "description": "예약 가능한 날짜 보여주는 캘린더",
                        "example": ["2022-01-01", "2022-01-02"],
                    },
                    "image_urls": {
                        "type": "array",
                        "items": "string",
                        "description": "array의 첫번째 이미지 url이 썸네일 이미지",
                    },
                },
            },
        }
    },
}

room_guest_search = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "query",
            "name": "facilities",
            "schema": {
                "type": "array",
                "items": "boolean",
                "example": [3, 6, 7],
            },
            "description": "[수영장(pool), Wifi, Kitchen, laundry_machine, Free Parking lot, air_conditioner, workspace, iron, fitness equipment, breakfast]",
        },
        {
            "in": "query",
            "name": "checkin",
            "schema": {"type": "string", "example": "2022-01-01"},
            "description": "체크인 날짜 YYYY-MM-DD",
        },
        {
            "in": "query",
            "name": "checkout",
            "schema": {"type": "string", "example": "2022-01-01"},
            "description": "체크아웃 날짜 YYYY-MM-DD",
        },
        {
            "in": "query",
            "name": "min_price",
            "schema": {"type": "integer", "example": 50000},
            "description": "최소가격",
        },
        {
            "in": "query",
            "name": "max_price",
            "schema": {"type": "integer", "example": 1000000},
            "description": "최대가격",
        },
        {
            "in": "query",
            "name": "type",
            "schema": {"type": "integer", "example": 1},
            "description": "숙소 유형 1: 아파트 2:주택 3: 별채 4:독특한숙소 5: B&B 6:부티크호텔",
        },
        {
            "in": "query",
            "name": "number_info",
            "schema": {"type": "array", "items": "integer", "example": [3, 2, 2, 2]},
            "description": "number_of_guests, number_of_beds, number_of_bedrooms, number_of_bathrooms",
        },
        {
            "in": "query",
            "name": "guest_area",
            "schema": {"type": "integer", "example": 1},
            "description": "게스트가 사용하는 공간범위(1:공간전체, 2:개인실, 3:다인실)",
        },
        {
            "in": "query",
            "name": "host_language",
            "schema": {"type": "string", "example": "korean"},
            "description": "호스트 언어",
        },
        {
            "in": "query",
            "name": "superhost",
            "schema": {"type": "boolean"},
            "description": "슈퍼 호스트 0:해당없음 1:해당",
        },
        {
            "in": "query",
            "name": "address_name",
            "schema": {"type": "string"},
            "description": "전체 지번 주소",
        },
        {
            "in": "query",
            "name": "center_coordinate",
            "schema": {
                "type": "array",
                "items": "number",
                "example": "36.1,127.5",
                "description": "중심 좌표",
            },
        },
        {
            "in": "query",
            "name": "radius",
            "schema": {
                "type": "number",
                "example": "12.33",
                "description": "반경(km)",
            },
        },
        {
            "in": "query",
            "name": "region_1depth_name",
            "schema": {"type": "string"},
            "description": "지역 1 Depth, 시도 단위",
        },
        {
            "in": "query",
            "name": "region_2depth_name",
            "schema": {"type": "string"},
            "description": "지역 2 Depth, 구 단위",
        },
        {
            "in": "query",
            "name": "region_3depth_name",
            "schema": {"type": "string"},
            "description": "지역 3 Depth, 동 단위",
        },
        {
            "in": "query",
            "name": "h_code",
            "schema": {"type": "integer"},
            "description": "행정 코드",
        },
        {
            "in": "query",
            "name": "b_code",
            "schema": {"type": "integer"},
            "description": "법정 코드",
        },
        {
            "in": "query",
            "name": "main_address_no",
            "schema": {"type": "integer"},
            "description": "지번 주번지",
        },
        {
            "in": "query",
            "name": "sub_address_no",
            "schema": {"type": "integer"},
            "description": "지번 부번지, 없을 경우 빈 문자열(" ") 반환",
        },
        {
            "in": "query",
            "name": "page",
            "schema": {"type": "integer"},
            "description": "페이지 번호",
        },
        {
            "in": "query",
            "name": "per_page",
            "schema": {"type": "integer"},
            "description": "페이지당 보여줄 숙소 개수",
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "rooms": {
                        "type": "array",
                        "items": {
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "숙소 id",
                                },
                                "type": {
                                    "type": "integer",
                                    "description": "숙소 유형",
                                },
                                "subtype": {
                                    "type": "integer",
                                    "description": "숙소를 가장 잘 설명하는 문구",
                                },
                                "guest_area": {
                                    "type": "integer",
                                    "description": "게스트가 사용하는 공간범위",
                                },
                                "number_info": {
                                    "type": "array",
                                    "items": "integer",
                                    "example": [5, 1, 1, 0],
                                    "description": "[number_of_guests, number_of_beds, number_of_bedrooms, number_of_bathrooms]",
                                },
                                "facilities": {
                                    "type": "array",
                                    "items": "integer",
                                    "example": [3, 6, 7],
                                    "description": "",
                                },
                                "address": {
                                    "type": "object",
                                    "properties": {
                                        "address_name": {
                                            "type": "string",
                                            "example": "서울 성동구 성수동2가 333-133",
                                        },
                                        "b_code": {
                                            "type": "integer",
                                            "example": 1120011500,
                                        },
                                        "h_code": {
                                            "type": "integer",
                                            "example": 1120067000,
                                        },
                                        "main_address_no": {
                                            "type": "integer",
                                            "example": 333,
                                        },
                                        "mountain_yn": {
                                            "type": "string",
                                            "example": "N",
                                        },
                                        "region_1depth_name": {
                                            "type": "string",
                                            "example": "서울",
                                        },
                                        "region_2depth_name": {
                                            "type": "string",
                                            "example": "성동구",
                                        },
                                        "region_3depth_name": {
                                            "type": "string",
                                            "example": "성수동2가",
                                        },
                                        "region_3depth_h_name": {
                                            "type": "string",
                                            "example": "성수2가1동",
                                        },
                                        "sub_address_no": {
                                            "type": "integer",
                                            "example": 133,
                                        },
                                        "x": {
                                            "type": "number",
                                            "example": 127.05334767117,
                                        },
                                        "y": {
                                            "type": "number",
                                            "example": 37.5402252730434,
                                        },
                                        "road_region_1depth_name": {
                                            "type": "string",
                                            "example": "서울",
                                        },
                                        "road_region_2depth_name": {
                                            "type": "string",
                                            "example": "성동구",
                                        },
                                        "road_region_3depth_name": {
                                            "type": "string",
                                            "example": "성수동2가",
                                        },
                                    },
                                },
                                "name": {
                                    "type": "string",
                                },
                                "specialties": {
                                    "type": "string",
                                },
                                "description": {
                                    "type": "string",
                                },
                                "price": {
                                    "type": "integer",
                                },
                                "others": {
                                    "type": "array",
                                    "items": "integer",
                                    "description": "0:security_camera, 1:weapon, 2:dangerous_animal",
                                    "example": [1],
                                },
                                "status": {
                                    "type": "string",
                                },
                                "user_id": {
                                    "type": "integer",
                                },
                                "superhost": {
                                    "type": "boolean",
                                    "description": "슈퍼 호스트 0:해당없음 1:해당",
                                },
                                "review": {
                                    "type": "object",
                                    "properties": {
                                        "review_point": {
                                            "type": "number",
                                            "description": "숙소 리뷰 평점"
                                        },
                                        "review_count": {
                                            "type": "integer",
                                            "description": "리뷰수",
                                        },
                                    }
                                },
                            }
                        },
                    },
                    "room_count": {"type": "integer", "description": "총 숙소 개수"},
                },
            },
        }
    },
}

room_reservation = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "게스트 숙소 예약",
            "required": True,
            "schema": {"$ref": "#/definitions/Room_Reservation"},
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
        }
    },
    "definitions": {
        "Room_Reservation": {
            "type": "object",
            "properties": {
                "room_id": {
                    "type": "integer",
                    "description": "숙소 id",
                },
                "check_in": {
                    "type": "string",
                    "description": "체크인 날짜",
                    "example": "2022-01-01",
                },
                "check_out": {
                    "type": "string",
                    "description": "체크아웃 날짜",
                    "example": "2022-01-02",
                },
                "price": {"type": "integer", "description": "1박 가격"},
                "number_of_guests": {"type": "integer"},
            },
        },
    },
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "reservation_id": {
                        "type": "integer",
                        "description": "예약 id",
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "유저 id",
                    },
                    "room_id": {
                        "type": "integer",
                        "description": "숙소 id",
                    },
                    "check_in": {
                        "type": "integer",
                        "description": "체크인 날짜",
                    },
                    "check_out": {
                        "type": "integer",
                        "description": "체크아웃 날짜",
                    },
                    "number_of_guests": {"type": "integer"},
                },
            },
        }
    },
}


host_search_reservation = {
    "tags": ["room/host"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "query",
            "name": "reservation_status",
            "schema": {"type": "integer"},
            "description": "1: 현재 호스팅 중 2: 체크인 예정 3:체크아웃 예정 4:예정 아무것도 입력하지 않으면 1,2,3,4에 해당하는 숙소 모두 불러옴",
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
        }
    },
}


room_close = {
    "tags": ["room/host"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "room_id",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소 차단날짜 설정",
            "required": True,
            "schema": {"$ref": "#/definitions/Room_Close"},
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
        }
    },
    "definitions": {
        "Room_Close": {
            "type": "object",
            "properties": {
                "closed_dates": {
                    "type": "array",
                    "items": "string",
                    "description": "차단 날짜 리스트",
                    "example": ["2022-01-01", "2022-01-02"],
                },
            },
        },
    },
}


cancel_reservation = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "reservation_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
        }
    },
}

reservation_list = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "query",
            "name": "reservation_status",
            "schema": {"type": "integer"},
            "description": "0: 체크인 전(예약된 일정), 1:투숙중(진행중인 일정) 2:체크아웃(이전여행지) 3:취소(취소된 일정)",
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "integer",
                            "description": "예약 id",
                        },
                        "user_id": {
                            "type": "integer",
                            "description": "유저 id",
                        },
                        "nickname": {
                            "type": "string",
                            "description": "호스트 닉네임",
                        },
                        "nickname": {
                            "type": "string",
                            "description": "호스트 닉네임",
                        },
                        "city": {
                            "type": "string",
                            "description": "도시 이름",
                        },
                        "check_in": {
                            "type": "string",
                            "description": "체크인 날짜",
                            "example": "2022-01-01",
                        },
                        "check_out": {
                            "type": "string",
                            "description": "체크아웃 날짜",
                            "example": "2022-01-02",
                        },
                    },
                },
            },
        }
    },
}

change_reservation = {
    "tags": ["room/guest"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "reservation_id",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소 예약 변경 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/Room"},
        },
    ],
    "responses": {
        "200": {
            "description": "successful operation",
        }
    },
    "definitions": {
        "Room": {
            "type": "object",
            "properties": {
                "check_in": {
                    "type": "string",
                    "description": "체크인 날짜 YYYY-MM-DD",
                    "example": "2022-01-01",
                },
                "check_out": {
                    "type": "string",
                    "description": "체크아웃 날짜 YYYY-MM-DD",
                    "example": "2022-01-02",
                },
                "number_of_guests": {
                    "type": "object",
                    "description": "adult:2, kid:1, infant:1, animal:0",
                    "properties": {
                        "adult": {"type": "integer"},
                        "kid": {"type": "integer"},
                        "infant": {"type": "integer"},
                        "animal": {"type": "integer"},
                    },
                },
            },
        }
    },
}

review_register = {
    "tags": ["host/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "room_id",
            "schema": {"type": "integer"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소 예약 변경 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/Review"},
        },
    ],
    "definitions": {
        "Review": {
            "type": "object",
            "properties": {
                "room_id": {
                    "type": "integer",
                    "description": "숙소 id",
                },
                "cleanness": {
                    "type": "integer",
                    "description": "청결도",
                },
                "accuracy": {
                    "type": "integer",
                    "description": "정확성",
                },
                "communication": {
                    "type": "integer",
                    "description": "의사소통",
                },
                "location": {
                    "type": "integer",
                    "description": "위치",
                },
                "checkin": {
                    "type": "integer",
                    "description": "체크인",
                },
                "satisfaction": {
                    "type": "integer",
                    "description": "가격대비만족도",
                },
                "message": {
                    "type": "string",
                    "description": "평가 내용",
                },
                "created_at": {
                    "type": "string",
                    "description": "생성일",
                },
            },
        }
    },
}


review_get = {
    "tags": ["host/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "review id",
        },
    ],
}

review_search = {
    "tags": ["host/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "user_id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "user id",
        },
        {
            "in": "path",
            "name": "room_id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "room id",
        },
    ],
}


review_delete = {
    "tags": ["host/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "review id",
        },
    ],
}

review_update = {
    "tags": ["host/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "review id",
        },
        {
            "in": "body",
            "name": "body",
            "description": "숙소 리뷰 수정 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/GuestReviewRegister"},
        },
    ],
    "definitions": {
        "Review": {
            "type": "object",
            "properties": {
                "cleanness": {
                    "type": "integer",
                    "description": "청결도",
                },
                "accuracy": {
                    "type": "integer",
                    "description": "정확성",
                },
                "communication": {
                    "type": "integer",
                    "description": "의사소통",
                },
                "location": {
                    "type": "integer",
                    "description": "위치",
                },
                "checkin": {
                    "type": "integer",
                    "description": "체크인",
                },
                "satisfaction": {
                    "type": "integer",
                    "description": "가격대비만족도",
                },
                "message": {
                    "type": "string",
                    "description": "평가 내용",
                },
            },
        }
    },
}


guest_review_register = {
    "tags": ["guest/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "body",
            "name": "body",
            "description": "게스트 리뷰 등록 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/GuestReviewRegister"},
        },
    ],
    "definitions": {
        "GuestReviewRegister": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "평가 내용",
                },
                "room_id": {"type": "integer", "description": "room id"},
                "guest_id": {"type": "integer", "description": "guest user_id"},
                "host_id": {"type": "integer", "description": "host user_id"},
            },
        }
    },
}


guest_review_search = {
    "tags": ["guest/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "user_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
}

guest_review_delete = {
    "tags": ["guest/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "review_id",
        },
    ],
}

guest_review_update = {
    "tags": ["guest/review"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
            "description": "review_id",
        },
        {
            "in": "body",
            "name": "body",
            "description": "리뷰 업데이트",
            "required": True,
            "schema": {"$ref": "#/definitions/GuestReview"},
        },
    ],
    "definitions": {
        "GuestReview": {
            "type": "object",
            "properties": {
                "message": {"type": "integer", "description": "review id"},
            },
        }
    },
}
