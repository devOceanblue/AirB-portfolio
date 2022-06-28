from sqlalchemy import text


class AddressRepository:
    def __init__(self):
        pass

    def get(self, id):
        from app import db_room

        with db_room.connect() as cnn:
            query = f"SELECT * FROM address WHERE address_id={id}"
            result = cnn.execute(text(query))
            result = result.first()
            result = dict(result)
        return result
