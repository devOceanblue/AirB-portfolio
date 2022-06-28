import calendar
import datetime
import json
import logging
from collections import defaultdict

from sqlalchemy import text
from typing import List


class RoomRepository:
    def register_address(self, address: dict):
        from app import db_room

        clauses = []
        for k, v in address.items():
            if not v:
                clauses.append(f"{k} = null")
            elif type(v) == str:
                clauses.append(f"{k} = {repr(v)}")
            else:
                clauses.append(f"{k} = {v}")
        create_clauses = ",".join(clauses)
        query = text(
            f"""
                 INSERT INTO address SET {create_clauses}
                 """
        )
        with db_room.connect() as cnn:
            cur = cnn.execute(query)
            return cur.lastrowid

    def create(self, args: dict):
        from app import db_room

        clauses = []
        for k, v in args.items():
            if not v:
                clauses.append(f"{k} = null")
            elif type(v) == str:
                clauses.append(f"{k} = {repr(v)}")
            else:
                clauses.append(f"{k} = {v}")
        create_clauses = ",".join(clauses)
        query = text(
            f"""INSERT INTO room SET {create_clauses}
                 """
        )
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            return result.lastrowid

    def get_review_stats(self, room_id):
        from app import db_room

        result = None
        with db_room.connect() as cnn:
            query = f"SELECT *, cleanness + accuracy + communication + location + checkin + satisfaction AS sum_point FROM review WHERE room_id={room_id}"
            result = cnn.execute(text(query))
            result = result.fetchall()
        if result:
            result = [dict(row) for row in result]
        else:
            return result
        stats = {
            "reviews": result,
            "review_point": sum([row["sum_point"] for row in result]) / len(result),
            "review_count": len(result),
        }
        return stats

    def get(self, id):
        from app import db_room

        with db_room.connect() as cnn:
            query = f"""SELECT r.*, GROUP_CONCAT(i.image_url) as image_urls
                        FROM room r LEFT JOIN room_images i ON r.id = i.room_id
                        WHERE r.id={id}
                        GROUP BY r.id, type, subtype, guest_area, number_of_guests, number_of_beds, number_of_bedrooms,
                                          number_of_bathrooms, pool, jacuzzi, patio, barbecue_grill, firepit, billiard_table, indoor_fireplace,
                                          outdoor_dining_area, fitness_equipment, wifi, tv, kitchen, laundry_machine, free_parking_lot,
                                          pay_parking_lot, air_conditioner, workspace, outdoor_shower_booth, fire_alarm, first_aid_kit,
                                          carbon_monoxide_alarm, fire_extinguisher, name, specialties, description, price, security_camera,
                                          weapon, dangerous_animal, country, city_id, state_id, address, status, coordinate, user_id, x, y,
                                          iron, breakfast, created_at, updated_at
                    """
            result = cnn.execute(text(query))
            result = result.first()
            result = dict(result)
        return result

    def get_rooms_result_for_guest(
        self,
        pool: int = None,
        jacuzzi: int = None,
        patio: int = None,
        barbecue_grill: int = None,
        firepit: int = None,
        billiard_table: int = None,
        indoor_fireplace: int = None,
        outdoor_dining_area: int = None,
        wifi: int = None,
        tv: int = None,
        kitchen: int = None,
        laundry_machine: int = None,
        free_parking_lot: int = None,
        pay_parking_lot: int = None,
        air_conditioner: int = None,
        workspace: int = None,
        outdoor_shower_booth: int = None,
        fire_alarm: int = None,
        first_aid_kit: int = None,
        carbon_monoxide_alarm: int = None,
        fire_extinguisher: int = None,
        iron: int = None,
        breakfast: int = None,
        fitness_equipment: int = None,
        checkin: str = None,
        checkout: str = None,
        min_price: int = None,
        max_price: int = None,
        type: int = None,
        number_of_guests: int = None,
        number_of_beds: int = None,
        number_of_bedrooms: int = None,
        number_of_bathrooms: int = None,
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
        def _get_where_clauses():
            if checkin and checkout:
                clauses.append(
                    f"""
                            r.id not in(
                            SELECT s.*
                            FROM(
                            (SELECT 0)
                            UNION ALL
                            (SELECT room_id
                            FROM reservation
                            WHERE {checkout} > DATE(check_in) AND {checkin} < DATE(check_out))
                            UNION ALL
                            (SELECT room_id
                            FROM closed_dates
                            WHERE {checkout} != closed_date AND {checkin} != closed_date))s
                        )
                        """
                )

            if min_price and max_price:
                clauses.append(f"price BETWEEN {min_price} AND {max_price}")

            if number_of_guests:
                clauses.append(f"number_of_guests >= {number_of_guests}")

            if number_of_beds:
                clauses.append(f"number_of_beds >= {number_of_beds}")

            if number_of_bedrooms:
                clauses.append(f"number_of_bedrooms >= {number_of_bedrooms}")

            if number_of_bathrooms:
                clauses.append(f"number_of_bathrooms >= {number_of_bathrooms}")

            if guest_area:
                clauses.append(f"guest_area = {guest_area}")

            if host_language:
                clauses.append(f"""JSON_CONTAINS(language, '"{host_language}"')""")

            if superhost:
                clauses.append(f"role = 'superhost'")

            if address_name:
                clauses.append(f"address_name = '{address_name}'")

            '''
            if center_coordinate:
                polygons = [f"{coordinate_boundary[idx]} {coordinate_boundary[idx+1]} " for idx in range(0,len(coordinate_boundary),2)]
                geom = ','.join(polygons)
                clauses.append(f"""ST_GeomFromText('Polygon(({geom}))')""")
            '''

            if region_1depth_name:
                clauses.append(f"region_1depth_name = '{region_1depth_name}'")

            if region_2depth_name:
                clauses.append(f"region_2depth_name = '{region_2depth_name}'")

            if region_3depth_name:
                clauses.append(f"region_3depth_name = '{region_3depth_name}'")

            if h_code:
                clauses.append(f"h_code = {h_code}")

            if b_code:
                clauses.append(f"b_code = {b_code}")

            if main_address_no:
                clauses.append(f"main_address_no = {main_address_no}")

            if sub_address_no:
                clauses.append(f"sub_address_no = {sub_address_no}")
            where_clauses = "  AND  ".join(clauses)
            if where_clauses:
                where_clauses = f"WHERE {where_clauses}"
            return where_clauses

        from app import db_room

        clauses = []
        where_clauses = _get_where_clauses()
        limit_clauses = f" LIMIT {str(int(page)-1)},{str(per_page)}"

        rows = None
        with db_room.connect() as cnn:
            query = f"""
                    SELECT Json_object("address_name", address_name, "b_code", b_code, "h_code",
                           h_code,
                                  "main_address_no", main_address_no, "mountain_yn", mountain_yn,
                                  "region_1depth_name", region_1depth_name, "region_2depth_name",
                                  region_2depth_name, "region_3depth_h_name", region_3depth_name,
                                  "region_3depth_name", region_3depth_h_name, "sub_address_no", sub_address_no, "x",
                           r.x, "y",
                                  r.y)                                            AS address,
                           description,
                           Json_array(pool, jacuzzi, patio, barbecue_grill, firepit, billiard_table,
                           indoor_fireplace, outdoor_dining_area, wifi, tv, kitchen, laundry_machine
                           ,
                           free_parking_lot, pay_parking_lot, air_conditioner, workspace,
                           outdoor_shower_booth, fire_alarm, first_aid_kit, carbon_monoxide_alarm,
                           fire_extinguisher, iron, breakfast, fitness_equipment) AS facilities,
                           guest_area,
                           r.id,
                           NAME,
                           Json_array(number_of_guests, number_of_beds, number_of_bedrooms,
                           number_of_bathrooms)                                   AS number_info,
                           Json_array(security_camera, weapon, dangerous_animal)  AS others,
                           price,
                           Count(v.id)                                            AS review_count,
                           Avg(v.cleanness + v.accuracy + v.communication
                               + v.location + v.checkin + v.satisfaction
                               + v.message)                                       AS review_point,
                           specialties,
                           subtype,
                           CASE
                             WHEN role = 'superhost' THEN true
                             ELSE false
                           END                                                    AS superhost,
                           type,
                           r.user_id,
                           JSON_ARRAYAGG(image_url) AS image_urls
                    FROM   room r
                           JOIN address a
                             ON r.address = a.address_id
                           JOIN (SELECT u.unique_id               AS user_id,
                                        Json_arrayagg(l.language) AS language,
                                        r.role
                                 FROM   airbnb_user.user AS u
                                        JOIN airbnb_user.user_role AS r
                                          ON u.role = r.id
                                        JOIN airbnb_user.user_language l
                                          ON u.unique_id = l.user_id
                                 GROUP  BY u.unique_id,
                                           r.role) b
                             ON r.user_id = b.user_id
                           LEFT JOIN review v
                                  ON r.id = v.room_id
                           LEFT JOIN room_images i ON r.id=i.room_id
                    {where_clauses}
                    GROUP  BY r.id
                    {limit_clauses};
            """
            qry = cnn.execute(text(query))
            rows = qry.fetchall()
        result = [dict(row) for row in rows] if rows else None
        for row in result:
            row['image_urls'] = json.loads(row['image_urls'])
            row['address'] = json.loads(row['address'])
        return result

    def register_filename(self, room_id, filenames: List[str]):
        from app import db_room

        create_clauses = [f"({room_id},{repr(filename)})" for filename in filenames]
        create_clauses = ",".join(create_clauses)
        query = text(
            f"""INSERT INTO room_images(room_id, image_url) VALUES {create_clauses}
                 """
        )
        with db_room.connect() as cnn:
            cnn.execute(query)
            return

    def search_number_of_guest_id(self, body: dict):
        from app import db_room

        adult = body.get("adult")
        kid = body.get("kid")
        infant = body.get("infant")
        animal = body.get("animal")

        query = text(
            f"""
            SELECT id
            FROM number_of_guests
            WHERE adult={adult} AND kid={kid} AND infant={infant} AND animal={animal}
            """
        )
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            return result.scalar()

    def search_number_of_guests(self, id):
        from app import db_room

        query = text(
            f"""
            SELECT adult, kid, infant, animal
            FROM number_of_guests
            WHERE id = {id}
            """
        )
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            return dict(result.first())

    def make_reservation(
        self,
        room_id: int,
        checkin: str,
        checkout: str,
        price: int,
        number_of_guests: int,
        user_id: int,
    ):
        from app import db_room

        query = text(
            f"""INSERT INTO reservation(user_id, room_id, check_in, check_out, price, status, number_of_guests)
            VALUES ({user_id}, {room_id}, {checkin}, {checkout}, {price}, 1, {number_of_guests})
                 """
        )
        with db_room.connect() as cnn:
            cnn.execute(query)
            return

    def close_room(self, body: dict = None):

        from app import db_room

        room_id = body.get("room_id")
        closed_dates = body.get("closed_date")

        insert_values_clauses = ",".join(
            [f"({closed_date}, {room_id})" for closed_date in body["closed_dates"]]
        )

        query = text(
            f"""
            INSERT INTO closed_dates(closed_date, room_id) VALUES {insert_values_clauses}
            """
        )
        with db_room.connect() as cnn:
            cnn.execute(query)
            return

    def cancel_reservation(self, reservation_id):
        from app import db_room

        query = text(f"""DELETE FROM reservation WHERE id = {reservation_id}""")
        with db_room.connect() as cnn:
            cnn.execute(query)
            return

    def get_reservation_list(self, user_id, reservation_status):
        from app import db_room

        query = text(
            f"""
            SELECT * FROM reservation WHERE user_id={user_id} AND status={reservation_status}
            """
        )
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info(query)
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            result = result.fetchall()
            if result:
                result = [dict(row) for row in result]
            return result

    def change_reservation(self, reservation_id, body):
        from app import db_room

        body["number_of_guests"] = self.search_number_of_guest_id(
            body.get("number_of_guests")
        )
        clauses = []
        for k, v in body.items():
            if type(v) == str:
                clauses.append(f"{k} = {repr(v)}")
            elif v is None:
                clauses.append(f"{k} = null")
            else:
                clauses.append(f"{k} = {v}")
        update_clauses = ",".join(clauses)
        query = text(
            f"""
            UPDATE reservation SET {update_clauses}
            """
        )
        with db_room.connect() as cnn:
            cnn.execute(query)
            return

    def host_search_reservation(self, user_id, reservation_status):
        from app import db_room

        query = text(
            f"""
            SELECT * FROM reservation AS v JOIN room AS m ON v.room_id = m.id WHERE m.user_id = {user_id} AND v.status = {reservation_status}
            """
        )
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            result = result.fetchall()
            if result:
                result = [dict(row) for row in result]
            return result

    def _get_dates_of_month(self, year, month):
        my_date = datetime.date(year, month, 1)
        delta = datetime.timedelta(days=1)
        dates = []

        while my_date.month == month:
            dates.append((my_date).strftime("%Y%m%d"))
            my_date += delta
        return dates

    def get_calendar(self, room_id):
        from app import db_room

        query = text(
            f"""
            SELECT DATE_FORMAT(check_in, '%Y%m%d') AS check_in, DATE_FORMAT(check_out, '%Y%m%d') AS check_out FROM reservation WHERE room_id = {room_id} AND check_in >='{datetime.datetime.today().date()}'ORDER BY check_in, check_out;
            """
        )
        result = None
        with db_room.connect() as cnn:
            result = cnn.execute(query)
            result = result.fetchall()
            if result:
                result = [dict(row) for row in result]

        today = datetime.datetime.today()
        year = today.year
        month = today.month
        calendar_of_365days = []
        for i in range(12):
            dates = self._get_dates_of_month(year, month)
            calendar_of_this_month = {date: [1, 1] for date in dates}

            for row in result:
                calendar_of_this_month[row["check_in"]][0] = 0
                calendar_of_this_month[row["check_out"]][1] = 0
                for i in range(int(row["check_in"]) + 1, int(row["check_out"])):
                    calendar_of_this_month[str(i)][0] = 0
                    calendar_of_this_month[str(i)][1] = 0
            calendar_of_365days.append(calendar_of_this_month)

            if month < 12:
                month += 1
            else:
                year += 1
                month = 1

        return calendar_of_365days
