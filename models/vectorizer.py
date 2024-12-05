
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, X):
        return self.vectorizer.fit_transform(X)

    def transform(self, X):
        return self.vectorizer.transform(X)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.vectorizer, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
