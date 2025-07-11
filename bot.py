from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '8080954224:AAFxo_pdJdEfvjoVf1xGb2dG-VulJPpach8'

def start(update, context):
    update.message.reply_text(
        "❤️ Welcome to Cyber Mafia's Bot!
"
        "DM me if you face any problem with my bots.
"
        "You can also ask me if you want any help."
    )

def help_command(update, context):
    update.message.reply_text('Send me Terabox video links!')

def echo(update, context):
    update.message.reply_text('✅ Link received! (Download logic not yet implemented)')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()