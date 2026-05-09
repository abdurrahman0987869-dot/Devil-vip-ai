from config import ADMIN_ID
from services.database import users, get_user, update_user

async def add_premium(update, context):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("No access.")
        return
    uid = int(context.args[0])
    users.update_one({"_id": uid}, {"$set": {"premium": True}})
    await update.message.reply_text(f"✅ User {uid} upgraded to premium!")

async def remove_premium(update, context):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("No access.")
        return
    uid = int(context.args[0])
    users.update_one({"_id": uid}, {"$set": {"premium": False}})
    await update.message.reply_text(f"❌ User {uid} is no longer premium.")

async def give_credits(update, context):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("No access.")
        return
    uid = int(context.args[0])
    amount = int(context.args[1])
    user = get_user(uid)
    user["credits"] += amount
    update_user(uid, user)
    await update.message.reply_text(f"💰 Gave {amount} credits to {uid}.")
    