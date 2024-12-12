import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

class ShanAI:
    def __init__(self):
        # Initialize the lemmatizer
        self.lemmatizer = WordNetLemmatizer()

    def identify_intent(self, text):
        # Tokenize the text
        tokens = word_tokenize(text)

        # Lemmatize the tokens
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        # Join the lemmatized tokens back into a string
        lemmatized_text = ' '.join(lemmatized_tokens)

        # Load the trained intent identification model
        with open('intent_identification_model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Use the model to predict the intent
        intent = model.predict([lemmatized_text])

        return intent

    def train_intent_identification_model(self, intents, labels):
        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Fit the vectorizer to the intents and transform them into vectors
        intent_vectors = vectorizer.fit_transform(intents)

        # Split the data into training and testing sets
        intent_train, intent_test, label_train, label_test = train_test_split(intent_vectors, labels, test_size=0.2, random_state=42)

        # Train a Multinomial Naive Bayes classifier on the training data
        model = MultinomialNB()
        model.fit(intent_train, label_train)

        # Save the trained model
        with open('intent_identification_model.pkl', 'wb') as f:
            pickle.dump(model, f)
