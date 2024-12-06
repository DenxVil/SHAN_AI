import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
token = '7845900356:AAEC59tP0_wVNwcWWfla_3iGSYqm8H0FQNM'
logging.basicConfig(level=logging.INFO)

TOKEN = '7845900356:AAEC59tP0_wVNwcWWfla_3iGSYqm8H0FQNM'  # Replace with your actual bot token

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello!')

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot = telegram.Bot(token) 
if __name__ == '__main__':
    main()


