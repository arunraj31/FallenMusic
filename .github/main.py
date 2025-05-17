from telegram.ext import Updater, CommandHandler

# Tumhara bot token
BOT_TOKEN = "7440242907:AAEAhud_e7KA2cJy_vV6GkFRaSaFFaaf924"

# Start command ka function
def start(update, context):
    update.message.reply_text("Hello! Bot is running successfully.")

# Main function to start bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Start command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
