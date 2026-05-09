from services.openai_api import generate_image
from services.database import get_user, update_user, log_event
from utils.rate_limiter import check_limit

async def handle_image(update, context):
    uid = update.effective_user.id
    prompt = " ".join(context.args)
    user = get_user(uid)

    if not user["premium"] and not check_limit(user, "daily_image"):
        await update.message.reply_text("🖼 Daily free image limit reached.")
        return

    url = generate_image(prompt)
    await update.message.reply_photo(url)

    user["daily_image"] += 1
    update_user(uid, user)
    log_event(uid, "image", prompt)
    