from dataclasses import dataclass


@dataclass
class User:
    id: str
    password: str
    email: str
    role: int
    nickname: str
    description: str
    sex: str
