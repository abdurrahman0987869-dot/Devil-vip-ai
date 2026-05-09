from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from services.database import get_user, update_user
from utils.menu import main_menu

async def cb_handler(update, context):
    q = update.callback_query
    uid = q.from_user.id
    user = get_user(uid)
    data = q.data

    if data == "chat_menu":
        context.user_data["mode"] = "chat"
        await q.message.reply_text("Send your message to AI ✍️")

    elif data == "img_menu":
        context.user_data["mode"] = "image"
        await q.message.reply_text("Send your image prompt 🏞️")

    elif data == "premium_menu":
        msg = (
            "⭐ Premium perks:\n"
            "- Unlimited chat & images\n"
            "- Faster responses\n"
            "Ask admin for activation."
        )
        await q.message.reply_text(msg)
    await q.answer()

async def text_router(update, context):
    mode = context.user_data.get("mode")
    if not mode:
        await update.message.reply_text(
            "Please select an option from menu.", reply_markup=main_menu()
        )
        