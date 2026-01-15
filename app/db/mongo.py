from pymongo import MongoClient
from datetime import datetime




MONGO_URL = "mongodb://root:root@localhost:27017"  
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["netops_db"]  
def log_device_event(device_id: int, message: str, severity: str = "INFO"):
 
    mongo_db.device_logs.insert_one({
        "device_id": device_id,
        "timestamp": datetime.utcnow(),
        "severity": severity,
        "message": message,
        "raw_data": {}
    })