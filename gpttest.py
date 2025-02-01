from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

# Directly set the Groq API key
API_KEY = "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"

# Initialize the Groq client with the API key
client = Groq(
    api_key=API_KEY,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # Create a chat completion request using Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    
    # Return the response from Groq
    return jsonify(chat_completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)