from pymongo import MongoClient

MONGO_URL = "mongodb://root:root@localhost:27017"  
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["netops_db"]  