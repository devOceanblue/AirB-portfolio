import logging

import bcrypt
from data.Models.user_repository import UserReposiotry
from entities.user import User
from typing import List


class UserService:
    def __init__(self):
        self.repo = UserReposiotry()

    def create_user(self, user: User):
        return self.repo.create_user(user)

    def _encrypt_password(self, password: str):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def _verify_password(self, password: str, hashpw: str):
        return bcrypt.checkpw(password.encode("utf-8"), hashpw.encode("utf-8"))

    def search(self, body: dict):
        return self.repo.search(body)

    def patch(self, id: str, body: dict):
        return self.repo.patch(id, body)

    def user_others_info(self, user_id):
        return self.repo.user_info(user_id)

    def user_profile_update(self):
        return self.repo.user_profile_update()

    def user_me_info(self, user_id):
        return self.repo.user_info(user_id)
