user_register = {
    "tags": ["user"],
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "description": "유저 등록",
            "required": True,
            "schema": {"$ref": "#/definitions/User"},
        }
    ],
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "password": {"type": "string"},
                "email": {"type": "string"},
            },
        }
    },
    "responses": {
        "201": {"description": "유저 등록 성공"},
        "422": {"description": "유저 등록 실패"},
    },
}

user_login = {
    "tags": ["user"],
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "description": "successfully login",
            "required": True,
            "schema": {"$ref": "#/definitions/User"},
        }
    ],
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "password": {"type": "string"},
                "email": {"type": "string"},
            },
        }
    },
    "responses": {
        "200": {
            "description": "User logged in",
            "schema": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string"},
                    "refresh_token": {
                        "type": "string",
                    },
                },
            },
        },
        "401": {"description": "UnAuthorized. 입력한 유저 정보가 맞지 않음"},
        "404": {"description": "유저 존재하지 않음"},
        "422": {"description": "유효하지 않은 입력 정보"},
    },
}

user_refresh = {
    "tags": ["user"],
    "summary": "유저 jwt refresh토큰 재발급",
    "description": "유저 jwt refresh토큰 재발급",
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        }
    ],
    "operationId": "refresh User",
    "produces": ["application/xml", "application/json"],
    "responses": {"200": {"description": "refreshUser"}},
}

user_logout = {
    "tags": ["user"],
    "summary": "Logs out current logged in user session",
    "description": "",
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        }
    ],
    "operationId": "logoutUser",
    "produces": ["application/xml", "application/json"],
    "responses": {"200": {"description": "successful operation"}},
}


user_me = {
    "tags": ["user"],
    "summary": "내 유저 정보",
    "description": "내 유저 정보",
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "unique_id": {
                        "type": "integer",
                        "description": "id",
                    },
                    "id": {
                        "type": "integer",
                        "description": "유저 id",
                    },
                    "email": {
                        "type": "string",
                    },
                    "role": {
                        "type": "string",
                        "description": "1:유저 2:호스트 3:매니저 4:슈퍼호스트",
                    },
                    "nickname": {
                        "type": "string",
                    },
                    "description": {
                        "type": "string",
                        "description": "호스트 자기소개",
                    },
                    "location": {"type": "string", "description": "유저 위치"},
                    "created_at": {
                        "type": "string",
                    },
                    "sex": {
                        "type": "string",
                    },
                    "birthday": {
                        "type": "string",
                    },
                    "phone_number": {
                        "type": "string",
                    },
                    "language": {
                        "type": "array",
                        "items": "string",
                        "description": "호스트 언어",
                    },
                },
            },
        }
    },
}

user_others = {
    "tags": ["user"],
    "summary": "다른 유저 정보",
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
        },
    ],
    "description": "다른 유저 정보",
    "responses": {
        "200": {
            "description": "successful operation",
            "schema": {
                "type": "object",
                "properties": {
                    "unique_id": {
                        "type": "integer",
                        "description": "id",
                    },
                    "id": {
                        "type": "integer",
                        "description": "유저 id",
                    },
                    "email": {
                        "type": "string",
                    },
                    "role": {
                        "type": "string",
                        "description": "1:유저 2:호스트 3:매니저 4:슈퍼호스트",
                    },
                    "nickname": {
                        "type": "string",
                    },
                    "description": {
                        "type": "string",
                        "description": "호스트 자기소개",
                    },
                    "location": {"type": "string", "description": "유저 위치"},
                    "created_at": {
                        "type": "string",
                    },
                    "sex": {
                        "type": "string",
                    },
                    "birthday": {
                        "type": "string",
                    },
                    "phone_number": {
                        "type": "string",
                    },
                    "language": {
                        "type": "array",
                        "items": "string",
                        "description": "호스트 언어",
                    },
                },
            },
        }
    },
}


user_profile_update = {
    "tags": ["user"],
    "summary": "유저프로필 업데이트",
    "description": "유저 프로필 업데이트",
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
            "description": "유저프로필 업데이트",
            "required": True,
            "schema": {"$ref": "#/definitions/UserProfileUpdate"},
        },
        {
            "in": "path",
            "name": "id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "definitions": {
        "UserProfileUpdate": {
            "type": "object",
            "properties": {
                "nickname": {"type": "string", "description": "실명"},
                "sex": {"type": "string", "description": "성별"},
                "birthday": {"type": "string", "description": "생년월일"},
                "email": {"type": "string", "description": "이메일"},
                "phone_number": {"type": "string", "description": "전화번호"},
                "location": {"type": "string", "description": "주소"},
            },
        }
    },
}
