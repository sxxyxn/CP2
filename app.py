#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template, request, jsonify
import chatbot

application = Flask(__name__, static_url_path='')

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/chatting', methods=['GET', 'POST'])
def chatting():
    message = request.json['message']
    messages = chatbot.chatbot_response(message)
    return jsonify({'message': messages})

if __name__ == '__main__':
    
    application.run(host='0.0.0.0')
