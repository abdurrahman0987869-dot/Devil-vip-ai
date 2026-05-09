from utils.menu import main_menu
from services.database import get_user

async def start(update, context):
    uid = update.effective_user.id
    get_user(uid)
    await update.message.reply_text("🤖 Welcome to your AI bot!", reply_markup=main_menu())
    