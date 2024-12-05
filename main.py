
# Solely coded by Denvil ♥️



from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from transformers import LLaMATokenizer, LLaMAForConditionalGeneration
import torch
import os

# Load pre-trained LLaMA model and tokenizer
model = LLaMAForConditionalGeneration.from_pretrained("decapoda-research/llama-7b")
tokenizer = LLaMATokenizer.from_pretrained("decapoda-research/llama-7b")

def generate_text(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
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
    token = os.getenv("TOKEN")
    if token is None:
        print("TOKEN environment variable is not set.")
        return

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
