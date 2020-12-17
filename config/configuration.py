import os
import dotenv
from pymongo import MongoClient
dotenv.load_dotenv()

client = MongoClient('mongodb://localhost/project_final')
db = client.get_database()
collection = db.get_collection("restaurants_final1")