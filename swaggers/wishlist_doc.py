wishlist_register = {
    "tags": ["wishlist"],
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
            "description": "위시리스트 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/WishlistRegister"},
        },
    ],
    "definitions": {
        "WishlistRegister": {
            "type": "object",
            "properties": {
                "room_id": {
                    "type": "integer",
                    "description": "위시리스트 숙소ID",
                },
                "wishlist_id": {
                    "type": "integer",
                    "description": "위시리스트ID ",
                },
            },
        }
    },
}

wishlist_create = {
    "tags": ["wishlist"],
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
            "description": "위시리스트 등록 정보",
            "required": True,
            "schema": {"$ref": "#/definitions/WishlistCreate"},
        },
    ],
    "definitions": {
        "WishlistCreate": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "위시리스트 이름",
                },
            },
        }
    },
}


wishlist_search = {
    "tags": ["wishlist"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "wishlist_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
}


wishlist_user_search = {
    "tags": ["wishlist"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "user_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
    "responses": {
        "200": {
            "description": "유저 위시리스트 목록",
            "schema": {
                "type": "array",
                "items": {
                    "id": {"type": "integer", "description": "wisihlist id"},
                    "name": {
                        "type": "string",
                        "description": "wishlist 이름",
                    },
                },
                "example": [{"id": 1, "name": "마운틴뷰"}],
            },
        },
    },
}


wishlist_delete = {
    "tags": ["wishlist"],
    "parameters": [
        {
            "in": "header",
            "name": "Authorization",
            "schema": {"type": "string"},
            "required": True,
        },
        {
            "in": "path",
            "name": "wishlist_id",
            "schema": {"type": "integer"},
            "required": True,
        },
    ],
}
