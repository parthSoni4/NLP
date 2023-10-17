from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def one():
    data = request.get_json()
    print(data["message"])
    print("Received JSON object:", data)
    url = "https://parth7084.pythonanywhere.com/chat"
    headers = {"Content-Type": "application/json"}
    payload = {"message": data["message"]}
    print(payload)
    response = requests.post(url, headers=headers, json=payload)

# Parse the JSON response
    response_json = response.json()

# Display the chatbot's response
    print(response_json["output"])
    return response_json

if __name__ == '__main__':
    app.run(debug=True)
