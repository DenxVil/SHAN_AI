
# Solely coded by Denvil ♥️

`main.py`
```
import json
from models.classifier import Classifier
from preprocessing.text_preprocessing import preprocess_text
from profile_access.profile_access import access_profile
from response_generation.response_generation import generate_response

def main():
    # Load the ai_profile.json file
    with open('ai_profile.json') as file:
        profile_data = json.load(file)

    # Load the trained classifier
    classifier = Classifier.load('classifier.pkl')

    # Define a function to handle user input
    def handle_input(text):
        # Preprocess the input text
        text = preprocess_text(text)

        # Classify the input text
        intent = classifier.predict([text])[0]

        # Access the profile information
        profile_info = access_profile(profile_data, intent)

        # Generate a response
        response = generate_response(profile_info)

        return response

    # Test the handle_input function
    text = 'What is your name?'
    response = handle_input(text)
    print(response)

if __name__ == '__main__':
    main()
```


