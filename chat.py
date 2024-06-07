from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

app = Flask(__name__)

patterns = [
    (r'my name is (.*)', ('Hello %1! Let me help you with scheduling your classes. Give me your student ID',)),
    (r'my student ID is (.*)', ('Got it, your student ID is %1. What is your major?',)),
    (r'my major is (.*)', ('Thanks for sharing your major. Which semester are you currently in?',)),
    (r'my semester is (.*)', ('Understood. Are there any specific preferences you have for class times?',)),
    (r'my preferences is (.*)', ('Noted. How might your commitments affect your class availability?',)),
    (r'my commitments are (.*)', ('Thanks for sharing your commitments so we can have a better vision. Anything else to consider?',)),
    (r'consider (.*)', ('Understood. Are there any specific requirements for class formats?',)),
    (r'my requirements are (.*)', ('Noted. Do you have any preferences or constraints related to breaks between classes?',)),
    (r'(.*)', ('Thanks for letting me know.',))
]

# Initialize chatbot
chatbot = Chat(patterns, reflections)

@app.route('/')
def home():
    return render_template('./templates/Features.html')

@app.route('/chat.py', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = chatbot.respond(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 