from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # Read from environment variable

client = MongoClient(MONGO_URI)
db = client["notes_db"]
notes_collection = db["notes"]
