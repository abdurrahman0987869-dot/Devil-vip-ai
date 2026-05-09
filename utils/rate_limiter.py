import datetime
from services.database import update_user

FREE_CHAT_LIMIT = 30
FREE_IMAGE_LIMIT = 5

def reset_if_needed(user):
    today = str(datetime.date.today())
    if user["last_reset"] != today:
        user["last_reset"] = today
        user["daily_chat"] = 0
        user["daily_image"] = 0
        update_user(user["_id"], user)
    return user

def check_limit(user, kind):
    user = reset_if_needed(user)
    if user["premium"]:
        return True
    limit = FREE_CHAT_LIMIT if kind == "daily_chat" else FREE_IMAGE_LIMIT
    return user[kind] < limit
    