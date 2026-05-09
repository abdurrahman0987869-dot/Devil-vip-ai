from pymongo import MongoClient
from config import MONGO_URI
import datetime

client = MongoClient(MONGO_URI)
db = client["telegram_ai_bot"]
users = db.users
logs = db.logs

def get_user(uid):
    user = users.find_one({"_id": uid})
    if not user:
        user = {
            "_id": uid,
            "premium": False,
            "credits": 0,
            "daily_chat": 0,
            "daily_image": 0,
            "last_reset": str(datetime.date.today())
        }
        users.insert_one(user)
    return user

def update_user(uid, data):
    users.update_one({"_id": uid}, {"$set": data})

def log_event(uid, action, detail=""):
    logs.insert_one({
        "uid": uid,
        "action": action,
        "detail": detail,
        "time": datetime.datetime.utcnow()
    })
    