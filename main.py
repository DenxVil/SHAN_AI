
# Solely coded by Denvil ♥️



import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import sentencepiece

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TOKEN = "5762561230:AAHYeayO4kdUIPIMvJZrzv-x-qiJjpZpIgo"

# Model and Tokenizer
model_name = 't5-small'
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Initialize NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()

def generate_response(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def sentiment_analysis(input_text):
    sentiment_scores = sia.polarity_scores(input_text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = generate_response(user_text)
    sentiment = sentiment_analysis(user_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Response: {response}\nSentiment: {sentiment}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)
    echo_handler = MessageHandler(None, echo)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(echo_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
