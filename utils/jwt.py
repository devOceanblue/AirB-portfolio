import redis

# Setup our redis connection for storing the blocklisted tokens. You will probably
# want your redis instance configured to persist data to disk, so that a restart
# does not cause your application to forget that a JWT was revoked.
from flask_jwt_extended import create_access_token

jwt_redis_blocklist = redis.StrictRedis(
    host="redis", port=6379, db=0, decode_responses=True
)


class JWT_Service:
    @staticmethod
    def generate_access_token(id):
        return create_access_token(identity=id)

    @staticmethod
    def generate_refresh_token(id):
        return create_access_token(identity=id)
