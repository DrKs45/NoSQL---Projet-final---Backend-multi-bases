from fastapi import APIRouter
from app.db.redis_client import redis_client, get_device_status

router = APIRouter(prefix="/api/redis", tags=["redis"])

@router.get("/live-status")
def get_live_status():
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

@router.get("/{device_id}/status")
def get_status(device_id: int):


    status = get_device_status(device_id)
    if not status:
        return {"status": "not found"}
    return {"device_id": device_id, "status": status}
