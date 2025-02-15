from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://easeworkai_admin:easeworkai_password@localhost:27019/easeworkai_db?authSource=admin")

client = AsyncIOMotorClient(MONGO_URI)
db = client["easeworkai_db"]
users_collection = db["users"]  # Collection for storing user data
