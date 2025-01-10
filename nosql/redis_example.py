import redis


def main():
    # Connect to the Redis instance
    redis_client = redis.Redis(host="localhost", port=6379, db=0)

    # Upload some sample data
    redis_client.set("example_key", "Hello, Redis!")

    # See...
    print(redis_client.get("example_key"))
