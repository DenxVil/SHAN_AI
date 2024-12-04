
# Solely coded by Denvil ♥️



import torch
from transformers import BardForConditionalGeneration, BardTokenizer
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load pre-trained Bard model and tokenizer
model = BardForConditionalGeneration.from_pretrained('google/bard')
tokenizer = BardTokenizer.from_pretrained('google/bard')

def analyze_and_generate(input_text):
    # Preprocess input text
    inputs = tokenizer(input_text, return_tensors="pt")
    
    # Analyze input text
    outputs = model(**inputs)
    analysis = outputs.last_hidden_state[:, 0, :]
    
    # Generate response
    response = model.generate(inputs["input_ids"], max_length=100)
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)
    
    return analysis, response_text

# Define a function to handle Telegram updates
async def handle_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        input_text = update.message.text
        analysis, response = analyze_and_generate(input_text)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text("An error occurred. Please try again.")

# Define the main function
def main():
    # Initialize the Telegram bot
    application = ApplicationBuilder().token("5762561230:AAHYeayO4kdUIPIMvJZrzv-x-qiJjpZpIgo").build()

    # Define the command handlers
    start_handler = CommandHandler('start', lambda update, context: context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI."))
    help_handler = CommandHandler('help', lambda update, context: context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!"))

    # Define the message handler
    message_handler = MessageHandler(None, handle_update)

    # Add the handlers to the application
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(message_handler)

    # Run the application
    application.run_polling()

# Run the main function
if __name__ == '__main__':
    main()
