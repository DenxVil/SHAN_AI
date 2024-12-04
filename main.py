
# Solely coded by Denvil ♥️



import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import sentencepiece
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Model and Tokenizer
model_name = 't5-small'
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Initialize NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()

def generate_response(input_text: str) -> str:
    try:
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "Error generating response"

def sentiment_analysis(input_text: str) -> str:
    try:
        sentiment_scores = sia.polarity_scores(input_text)
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        return "Error analyzing sentiment"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm SHAN AI.")

def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can assist you with various tasks. Type 'hello' to get started!")

def echo(update, context):
    user_text = update.message.text
    response = generate_response(user_text)
    sentiment = sentiment_analysis(user_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Response: {response}\nSentiment: {sentiment}")

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
