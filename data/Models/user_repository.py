import logging

from sqlalchemy import text
from entities.user import User


class UserReposiotry:
    def search(self, body: dict):
        from app import db_user

        clauses = []
        for k, v in body.items():
            if type(v) == str:
                clauses.append(f"{k}={repr(v)}")
            elif v is None:
                clauses.append(f"{k}=null")
            else:
                clauses.append(f"{k}={v}")
        where_clauses = f'WHERE {" AND ".join(clauses)}'

        with db_user.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                SELECT * FROM user {where_clauses}
                """
                )
            )
            result = result.first()
            result = dict(result) if result else None
            return result

    def create_user(self, user: User):
        from app import db_user

        id = repr(user.id)
        password = repr(user.password)
        email = repr(user.email)
        role = int(user.role)
        nickname = repr(user.nickname)
        description = repr(user.description)
        sex = repr(user.sex)

        with db_user.connect() as cnn:
            cnn.execute(
                text(
                    f"""
                INSERT INTO user(id,password,email,isVerified,role,nickname,description,sex) VALUES ({id},{password},{email},1,{role},{nickname},{description},{sex})
                """
                )
            )
            return

    def patch(self, id: str, body: dict):
        from app import db_user

        id = repr(id)
        clauses = []
        logging.info(f"body1:{body}")
        for k, v in body.items():
            logging.info(f"body:{v}")
            if type(v) == str:
                clauses.append(f"{k} = {repr(v)}")
            elif v is None:
                clauses.append(f"{k} = null")
            else:
                clauses.append(f"{k} = {v}")
        logging.info(clauses)
        update_clauses = ",".join(clauses)
        logging.info(update_clauses)

        with db_user.connect() as cnn:
            cnn.execute(
                text(
                    f"""
                UPDATE user SET {update_clauses} WHERE unique_id={id}
                """
                )
            )
            return

    def user_info(self, user_id):
        from app import db_user

        with db_user.connect() as cnn:
            result = cnn.execute(
                text(
                    f"""
                    SELECT unique_id, u.id, email, r.role, nickname, description, location, created_at, sex, birthday, phone_number, GROUP_CONCAT(l.language) as language
                    FROM user u JOIN user_role r ON u.role = r.id LEFT JOIN user_language l ON u.unique_id = l.user_id
                    WHERE unique_id = {user_id}
                    GROUP BY unique_id, id, email, role, nickname, description, location, created_at, sex, birthday, phone_number;
                    """
                )
            )
            result = result.first()
            result = dict(result) if result else None
            return result

    def user_profile_update(self):
        return
