from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dictionary containing predefined responses for specific inputs
responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thank you!",
    "bye": "Goodbye!",
    "default": "I'm sorry, I don't understand.",
    "aadya" : "Oh a mental girl",
    "what is grape" : "Grape is a small tech start up by three friends in late December of 2023, Arun Shreyas, Vedesh and Inian",
    "if x^2 = 9 what is x": "x is 3 as the root of 9 == 3 "

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user input from the request
    user_input = request.json['message'].lower()
    
    # Retrieve the appropriate response from the dictionary
    response = responses.get(user_input, responses["default"])
    
    # Return the response as JSON
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(debug=True)