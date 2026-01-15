from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.db.mongo import mongo_db

router = APIRouter(prefix="/api")

@router.get("/device/{device_id}/logs")
def get_device_logs(device_id: int, severity: Optional[str] = None, limit: Optional[int] = 100):
    """
    Récupère les logs d'un device depuis MongoDB
    """
    query = {"device_id": device_id}
    if severity:
        query["severity"] = severity

    logs = list(mongo_db.device_logs.find(query).sort("timestamp", -1).limit(limit))

   
    for log in logs:
        log["_id"] = str(log["_id"])

    return logs


class LogIngest(BaseModel):
    device_id: int
    severity: str
    message: str
    raw_data: dict = {}

@router.post("/logs/ingest")
def ingest_log(log: LogIngest):
 
    mongo_db.device_logs.insert_one({
        "device_id": log.device_id,
        "timestamp": datetime.utcnow(),
        "severity": log.severity,
        "message": log.message,
        "raw_data": log.raw_data
    })
    return {"status": "ok", "device_id": log.device_id}

@router.get("/logs")
def get_all_logs(limit: Optional[int] = 500):
   
    logs = list(mongo_db.device_logs.find().sort("timestamp", -1).limit(limit))

   
    for log in logs:
        log["_id"] = str(log["_id"])

    return logs
