import redis.asyncio as redis

# Connect to local Redis instance
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
