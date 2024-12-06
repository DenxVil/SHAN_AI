
# Solely coded by Denvil ♥️


from models.classifier import Classifier
from preprocessing.text_preprocessing import preprocess_text
from profile_access.profile_access import ProfileAccess
from response_generation.response_generation import ResponseGenerator
from telegram_bot.bot import TelegramBot

def main():
    try:
        # Initialize classifier
        classifier = Classifier()

        # Initialize profile access
        profile_access = ProfileAccess()

        # Initialize response generator
        response_generator = ResponseGenerator()

        # Initialize Telegram bot
        bot = Bot()

        # Start the bot
        bot.start()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
