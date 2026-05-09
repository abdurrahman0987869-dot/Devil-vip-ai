from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import BOT_TOKEN
from handlers import admin, chat, image, callbacks, general

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", general.start))
    app.add_handler(CommandHandler("chat", chat.handle_chat))
    app.add_handler(CommandHandler("image", image.handle_image))
    app.add_handler(CommandHandler("addpremium", admin.add_premium))
    app.add_handler(CommandHandler("removepremium", admin.remove_premium))
    app.add_handler(CommandHandler("givecredits", admin.give_credits))

    # Inline buttons + messages
    app.add_handler(CallbackQueryHandler(callbacks.cb_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callbacks.text_router))

    app.run_polling()

if __name__ == "__main__":
    main()
    