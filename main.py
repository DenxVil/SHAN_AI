
# Solely coded by Denvil ♥️



from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from together import Together

# API Keys
TELEGRAM_API_KEY = "5762561230:AAHYeayO4kdUIPIMvJZrzv-x-qiJjpZpIgo"
TOGETHER_API_KEY = "8cd3d00fab20dcaf04639e52cf553ce5052c81d0572b78b6becdd08ae4e8e951"

# Create a Together client
client = Together(api_key=TOGETHER_API_KEY)

# Telegram bot commands
async def start(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI.")

async def help(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!")

async def handle_message(update: Update, context: ContextTypes):
    input_text = update.message.text
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        messages=[{"role": "user", "content": input_text}],
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].message.content)

def main():
    # Create Telegram application
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    # Define command handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    message_handler = MessageHandler(None, handle_message)

    # Add handlers to application
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)

    # Run application
    application.run_polling()

if __name__ == '__main__':
    main()
