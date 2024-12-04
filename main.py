import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import torch
from llama import LLaMA, Tokenizer

model = LLaMA(model_name="llama-3.2", device="cuda" if torch.cuda.is_available() else "cpu")
tokenizer = Tokenizer(model_name="llama-3.2")

TOKEN = "5762561230:AAHYeayO4kdUIPIMvJZrzv-x-qiJjpZpIgo"

logging.basicConfig(level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your chatbot.")

def handle_message(update, context):
    message = update.message.text
    response = model.generate(tokenizer.encode(message, return_tensors="pt"), max_length=100)
    response = tokenizer.decode(response[0], skip_special_tokens=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
