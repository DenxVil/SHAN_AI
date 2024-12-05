
# Solely coded by Denvil ♥️



import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

def generate_text(input_text):
    api_endpoint = "https://api.together.xyz/models/llama"
    api_key = "8cd3d00fab20dcaf04639e52cf553ce5052c81d0572b78b6becdd08ae4e8e951"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"prompt": input_text}
    response = requests.post(api_endpoint, headers=headers, json=data)
    response_text = response.json()["response"]
    return response_text

def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI.")

def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!")

def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = update.message.text
    response = generate_text(input_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    token = "8cd3d00fab20dcaf04639e52cf553ce5052c81d0572b78b6becdd08ae4e8e951"
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    message_handler = MessageHandler(None, handle_message)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
