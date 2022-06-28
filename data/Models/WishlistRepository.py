from sqlalchemy import text


class WishlistRepository:
    def register_wishlist(self, body):
        from app import db_room

        room_id = body.get("room_id")
        wishlist_id = body.get("wishlist_id")

        with db_room.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                INSERT INTO wishlisted_rooms(wishlist_id, room_id) VALUES ({wishlist_id}, {room_id})
                """
                )
            )
            return result.lastrowid

    def search_wishlist(self, id):
        from app import db_room

        with db_room.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                SELECT * FROM wishlisted_rooms WHERE wishlist_id = {id}
                """
                )
            )
            return [dict(r) for r in result.all()]

    def delete_wishlist(self, id):
        from app import db_room

        with db_room.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                DELETE FROM wishlist WHERE wishlist_id = {id}
                """
                )
            )
            return [dict(r) for r in result.all()]

    def search_user_wishlist(self, user_id):
        from app import db_room

        with db_room.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                SELECT * FROM wishlist WHERE user_id = {user_id}
                """
                )
            )
            return [dict(r) for r in result.all()]

    def create_wishlist(self, user_id, body):
        from app import db_room

        name = body.get("name")

        with db_room.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                INSERT INTO wishlist(user_id, name) VALUES ({user_id}, {repr(name)})
                """
                )
            )
            return result.lastrowid
