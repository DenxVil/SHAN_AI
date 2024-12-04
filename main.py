
# Solely coded by Denvil ♥️



import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

# Initialize NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()

# Define a function to generate responses
def generate_response(input_text, sentiment):
    if sentiment == "Positive":
        response = "That's great to hear! What's making you happy today?"
    elif sentiment == "Negative":
        response = "Sorry to hear that. Would you like to talk about what's bothering you?"
    else:
        response = "That's interesting! Can you tell me more about it?"
    
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100)
    generated_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response + " " + generated_response

# Define a function to analyze sentiment
def sentiment_analysis(input_text):
    sentiment_scores = sia.polarity_scores(input_text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Define a function to handle Telegram updates
async def handle_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        input_text = update.message.text
        sentiment = sentiment_analysis(input_text)
        response = generate_response(input_text, sentiment)
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
