from services.openai_api import generate_text
from services.database import get_user, update_user, log_event
from utils.rate_limiter import check_limit

async def handle_chat(update, context):
    uid = update.effective_user.id
    msg = " ".join(context.args)
    user = get_user(uid)

    if not check_limit(user, "daily_chat"):
        await update.message.reply_text("💬 Daily chat limit reached.")
        return

    reply = generate_text(msg)
    await update.message.reply_text(reply)

    user["daily_chat"] += 1
    update_user(uid, user)
    log_event(uid, "chat", msg)
