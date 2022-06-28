from app import db_user
import bcrypt
import logging


class User(db_user.Model):
    id = db_user.Column(db_user.String(16), primary_key=True)
    password = db_user.Column(db_user.String(80), nullable=False)
    email = db_user.Column(db_user.String(30), unique=True, nullable=False)
    isVerified = db_user.Column(db_user.Boolean, nullable=False, default=False)

    def __init__(self, id, password, email):
        self.id = id
        self.password = password
        self.email = email

    def create(self):
        db_user.session.add(self)
        db_user.session.commit()
        logging.debug("hello!")
        return self

    @staticmethod
    def encrypt_password(password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(password, hashpw):
        return bcrypt.checkpw(password.encode("utf-8"), hashpw.encode("utf-8"))

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
