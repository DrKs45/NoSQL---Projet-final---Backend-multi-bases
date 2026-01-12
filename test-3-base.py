# PostgreSQL
import psycopg2

# MongoDB
from pymongo import MongoClient

# Redis
import redis

print("=== PostgreSQL ===")
pg = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="postgres"
)
cur = pg.cursor()
cur.execute("SELECT 1;")
print("Postgres OK:", cur.fetchone())
cur.close()
pg.close()

print("\n=== MongoDB ===")
mongo = MongoClient(
    "mongodb://root:root@localhost:27017/"
)
db = mongo["netops"]
print("Mongo OK, collections:", db.list_collection_names())

print("\n=== Redis ===")
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
print("Redis ping:", r.ping())
