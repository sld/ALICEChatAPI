#!/usr/bin/env python

from flask import Flask, request
from flask import render_template
import ai

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/respond", methods=['POST'])
def respond():
    bot.speakResponse(request.form['input'])
    return app.send_static_file('index.html')

if __name__ == '__main__':
    bot = ai.Chatbot()
    bot.initialize("aiml-dir")
    app.run(debug=True, host='0.0.0.0', port=3000)