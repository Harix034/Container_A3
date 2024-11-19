from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('MESSAGE', '') 
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
