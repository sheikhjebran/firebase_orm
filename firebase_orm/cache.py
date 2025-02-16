import redis
import json
from .settings import REDIS_HOST, REDIS_PORT


class CacheManager:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def set(self, key, value, expiry=3600):
        self.client.set(key, json.dumps(value), ex=expiry)

    def get(self, key):
        data = self.client.get(key)
        return json.loads(data) if data else None

    def delete(self, key):
        self.client.delete(key)
