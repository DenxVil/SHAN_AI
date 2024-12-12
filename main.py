
# Solely coded by Denvil ♥️




    
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import pickle
import json

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

# Load the intents
with open('intents.json') as f:
    intents = json.load(f)

# Extract the patterns and tags
patterns = [preprocess_text(pattern) for intent in intents['intents'] for pattern in intent['patterns']]
tags = [intent['tag'] for intent in intents['intents'] for _ in intent['patterns']]

# Create a TF-IDF vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the patterns and transform them into vectors
pattern_vectors = vectorizer.fit_transform(patterns)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
pattern_train, pattern_test, tag_train, tag_test = train_test_split(pattern_vectors, tags, test_size=0.2, random_state=42)

# Train a Multinomial Naive Bayes classifier on the training data
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(pattern_train, tag_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

def main():
    # Load the trained model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    while True:
        try:
            # Get user input
            user_input = input("User: ")
        except EOFError:
            user_input = "hello"  # provide a default input
            print("User: ", user_input)

        # Preprocess the user input
        user_input = preprocess_text(user_input)

        # Create a TF-IDF vector for the user input
        user_input_vector = vectorizer.transform([user_input])

        # Use the model to predict the tag
        predicted_tag = model.predict(user_input_vector)

        # Find the corresponding response
        for intent in intents['intents']:
            if intent['tag'] == predicted_tag[0]:
                response = intent['responses'][0]
                break

        # Print the response
        print("SHAN: ", response)
        break  # exit the loop after one iteration

if __name__ == "__main__":
    main()
