import redis

REDIS_URL = "redis://localhost:6379/0" 
redis_client = redis.Redis.from_url(REDIS_URL)



def set_device_status(device_id: int, status: str):
   
    key = f"device:{device_id}:status"
    redis_client.set(key, status)

def get_device_status(device_id: int):
    key = f"device:{device_id}:status"
    return redis_client.get(key)

def get_():
    statuses = {}
    cursor = 0

    while True:
        cursor, keys = redis_client.scan(cursor=cursor, match="device:*:status")
        for key in keys:
            device_id = int(key.decode().split(":")[1])
            statuses[device_id] = redis_client.get(key)
        if cursor == 0:
            break

    return statuses