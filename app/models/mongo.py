from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient(
    "mongodb://root:root@localhost:27017/?authSource=admin"
)

db = client["netops"]

db.device_logs.create_index(
    [("device_id_sql", ASCENDING), ("timestamp", DESCENDING)]
)
db.device_logs.create_index([("severity", ASCENDING)])

db.device_configs.create_index(
    [("device_id", ASCENDING), ("version", DESCENDING)]
)


print("MongoDB NetOps prêt")
