# -*- coding: utf-8 -*-
import requests


API_HOST = "http://dapi.kakao.com/v2/local/search/category.json"
headers = {"Authorization": ""}

#####엑셀#######
FROM = 2
TO = 5862
NAME = "H"
ADDRESS = "N"


###############


def req_query(query):
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={query}"
    return requests.get(url, headers=headers)


def req_category():
    category_list = ["MT1"]

    for category in category_list:
        url = f"https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category}"
        return requests.get(url, headers=headers)


def to_csv(rows):
    import csv

    # csv header
    fieldnames = [
        "address_name",
        "x",
        "y",
        "region_1depth_name",
        "region_2depth_name",
        "region_3depth_name",
        "region_3depth_h_name",
        "b_code",
        "h_code",
        "main_address_no",
        "sub_address_no",
        "road_region_1depth_name",
        "road_region_2depth_name",
        "road_region_3depth_name",
        "mountain_yn",
    ]

    # csv data

    with open("kakao_address.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    category_addresses = req_category().json()
    rows = []
    for i in range(1, 5):
        row = req_query(category_addresses["documents"][i]["address_name"]).json()
        row["documents"][0]["address"]["road_region_1depth_name"] = row["documents"][0][
            "road_address"
        ]["region_1depth_name"]
        row["documents"][0]["address"]["road_region_2depth_name"] = row["documents"][0][
            "road_address"
        ]["region_2depth_name"]
        row["documents"][0]["address"]["road_region_3depth_name"] = row["documents"][0][
            "road_address"
        ]["region_3depth_name"]
        rows.append(row["documents"][0]["address"])
    to_csv(rows)
