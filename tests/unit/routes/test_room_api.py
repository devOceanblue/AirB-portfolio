import random

def test_create_empty_folder(test_cli, monkeypatch):
    from google.cloud import storage

    monkeypatch.setenv("GOOGLE_APPLICATION_CREDENTIALS", "../../../resources/key.json")
    gcs_client = storage.Client()
    bucket = gcs_client.get_bucket("airbnb_cloud_storage")
    blob = bucket.blob("testfolder/a")
    blob.delete()


def test_get_room(test_cli, test_header):
    resp = test_cli.get("/room/host/4", headers=test_header)
    assert resp.status_code == 200
    result = resp.json
    print(f"result:{result}")


def test_get_room(test_cli, test_header):
    resp = test_cli.get("/room/guest/88", headers=test_header)
    assert resp.status_code == 200
    result = resp.json
    print(f"result:{result}")


def test_create(test_cli, test_header):
    dat = {
        "type": "4",
        "subtype": "6",
        "guest_area": "2",
        "address": {
            "address_name": "서울 강북구 우이동 산 40-1",
            "b_code": "1130510400",
            "h_code": "1130564500",
            "main_address_no": "40",
            "mountain_yn": 1,
            "region_1depth_name": "서울",
            "region_2depth_name": "강북구",
            "region_3depth_h_name": "우이동",
            "region_3depth_name": "우이동",
            "sub_address_no": "1",
            "x": "127.009646711804",
            "y": "37.6592414242173",
            "state": "",
            "country": "korea",
        },
        "number_info": {
            "number_of_guests": 5,
            "number_of_beds": 3,
            "number_of_bedrooms": 0,
            "number_of_bathrooms": 0,
        },
        "facilities": "12",
        "image_urls": [
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2Fkakao_recommend_friends.png?alt=media&token=dda8eb38-a27e-4a56-beed-68703c7e0e35",
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2FScreen%20Shot%200004-05-09%20at%2011.48.11%20AM.png?alt=media&token=9104746c-940f-4fcf-860d-61d488cbac5d",
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2FScreen%20Shot%200004-05-09%20at%2011.50.04%20AM.png?alt=media&token=a426cce2-9610-426b-a2bd-3df3963f06d4",
        ],
        "name": "sdfsdfdsfds",
        "description": "jkkj",
        "price": "5",
        "others": {"dangerous_animal": 0, "security_camera": 1, "weapon": 1},
    }

    resp = test_cli.post("/room/host", json=dat, headers=test_header)
    assert resp.status_code == 200
    print(f"result:{resp.json}")


def test_create_1000_rooms(test_cli, test_header):
    dat = {
        "type": f"{random.randrange(1,7)}",
        "subtype": f"{random.randrange(1,80)}",
        "guest_area": f"{random.randrange(1,4)}",
        "number_info": {
            "number_of_guests": random.randrange(1,10),
            "number_of_beds": random.randrange(2,8),
            "number_of_bedrooms": random.randrange(1,2),
            "number_of_bathrooms": random.randrange(1,3),
        },
        "facilities": "12",
        "image_urls": [
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2Fkakao_recommend_friends.png?alt=media&token=dda8eb38-a27e-4a56-beed-68703c7e0e35",
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2FScreen%20Shot%200004-05-09%20at%2011.48.11%20AM.png?alt=media&token=9104746c-940f-4fcf-860d-61d488cbac5d",
            "https://firebasestorage.googleapis.com/v0/b/airbnb-service.appspot.com/o/room-images%2FScreen%20Shot%200004-05-09%20at%2011.50.04%20AM.png?alt=media&token=a426cce2-9610-426b-a2bd-3df3963f06d4",
        ],
        "name": "sdfsdfdsfds",
        "description": "jkkj",
        "price": "5",
        "others": {"dangerous_animal": 0, "security_camera": 1, "weapon": 1},
    }

    resp = test_cli.post("/room/host", json=dat, headers=test_header)
    assert resp.status_code == 200
    print(f"result:{resp.json}")


def test_search(test_cli, test_header):
    resp = test_cli.get("/room", headers=test_header)
    assert resp.status_code == 200


def test_guest_search(test_cli, test_header):
    params = {
        "facilities": "3,6,7",
        "min_price": 13000,
        "max_price": 10000000,
        "type": 4,
        "number_info": "5,3,1,1",
        "guest_area": 2,
        "host_language": "korean",
        "superhost": 0,
        "address_name": "서울 강북구 우이동 산 40-1",
        "center_coordinate": "36.1,127.5",
        "radius": 34.2,
        "region_1depth_name": "서울",
        "region_2depth_name": "강북구",
        "region_3depth_name": "우이동",
        "h_code": 1130564500,
        "b_code": 1130510400,
        "main_address_no": 40,
        "sub_address_no": 1,
        "page": 1,
        "per_page": 10,
    }
    resp = test_cli.get("/room/guest", query_string=params, headers=test_header)
    assert resp.status_code == 200
    result = resp.json
    print(f"result:{result}")


def test_make_reservation(test_cli, test_header):
    params = {
        "room_id": 4,
        "checkin": "2022-01-01",
        "checkout": "2022-01-03",
        "price": 13000,
    }
    resp = test_cli.post("/room/reservation", json=params, headers=test_header)
    assert resp.status_code == 200
    result = resp.json
    print(f"result:{result}")


def test_host_search_reservation(test_cli, test_header):
    resp = test_cli.get(
        "/room/host/reservation?reservation_status=1", headers=test_header
    )
    result = resp.json
    print(f"result:{result}")


def test_cancel_reservation(test_cli, test_header):
    resp = test_cli.delete("/room/guest/reservation/4", headers=test_header)


def test_make_reservation(test_cli, test_header):
    dat = {
        "check_in": "2022-01-01",
        "check_out": "2022-01-02",
        "number_of_guests": {"adult": 0, "animal": 0, "infant": 0, "kid": 0},
        "price": 0,
        "room_id": 4,
    }
    resp = test_cli.post("/room/guest/reservation", json=dat, headers=test_header)
    assert resp.status_code == 200
