from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
database = client[DB_NAME]

# Collections
users_collection = database["users"]
sevas_collection = database["sevas"]
submissions_collection = database["submissions"]