import nltk
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')


def preprocess_input(text):
    # Tokenization  = it breakdown the text into words or tokens
    tokens = word_tokenize(text.lower())
    # Remove stopwords  = remove stop-words like the , a , an ...
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization = reducing the words exple ; running => run
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmatized_tokens


def save_response(user_id, question, response):
    # Placeholder function to save response to database
    print(f"Saving response to database: User ID - {user_id}, Question - {question}, Response - {response}")
    
    
def test_preprocessing():
    text = "Hello, how are you doing today?"
    preprocessed_text = preprocess_input(text)
    print("Preprocessed text:", preprocessed_text)    
    
if __name__ == "__main__":
    download_nltk_resources()
    test_preprocessing()





import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client["university_course_planning"]

# Create or access a collection within the database
collection = db["user_responses"]

# Example document to insert into the collection
user_response = {
    "name": "John Doe",
    "student_id": "123456",
    "major": "Computer Science",
    "academic_year": "Senior",
    # Add more fields for other user responses...
}

# Insert the document into the collection
result = collection.insert_one(user_response)
print("User response inserted with ID:", result.inserted_id)