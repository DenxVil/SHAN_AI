
# Solely coded by Denvil ♥️




import os
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

TELEGRAM_API_KEY = "5762561230:AAHYeayO4kdUIPIMvJZrzv-x-qiJjpZpIgo"
TOGETHER_API_KEY = "8cd3d00fab20dcaf04639e52cf553ce5052c81d0572b78b6becdd08ae4e8e951"  # Replace with your Together API key

async def generate_text(input_text):
    api_endpoint = "https://api.together.xyz/models/llama"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_endpoint, headers=headers, json={"prompt": input_text}) as response:
            response_text = await response.json()
            return response_text["response"]

async def start(update: Update, context: ContextTypes.DEFAULT):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI.")

async def help(update: Update, context: ContextTypes.DEFAULT):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT):
    input_text = update.message.text
    response = await generate_text(input_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    message_handler = MessageHandler(None, handle_message)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
