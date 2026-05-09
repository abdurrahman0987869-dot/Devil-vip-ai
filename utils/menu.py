from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    kb = [
        [InlineKeyboardButton("💬 Chat with AI", callback_data="chat_menu")],
        [InlineKeyboardButton("🖼 Generate Image", callback_data="img_menu")],
        [InlineKeyboardButton("⭐ Premium Info", callback_data="premium_menu")]
    ]
    return InlineKeyboardMarkup(kb)
    