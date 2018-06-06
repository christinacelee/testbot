from flask import Flask
from flask import make_response, request

import json

import os

VERIFY_TOKEN = "say_friend_and_you_will_enter"

#init code
app = Flask(__name__)
##app.config['PAGE_ACCESS_TOKEN'] = os.environ.get['PAGE_ACCESS_TOKEN']


#actual API-handling code

##PAGE_ACCESS_TOKEN = app.config.get('PAGE_ACCESS_TOKEN')
@app.route('/')
def hello_world():
    return 'Hello, World!'


##Webhook: entry point for msgs sent to this bot
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args['hub.mode']
        token = request.args['hub.verify_token']
        challenge = request.args['hub.challenge']

        if mode and token:
            if (mode == 'subscribe' and token == VERIFY_TOKEN):
                print('WEBHOOK_VERIFIED')
                return challenge
            else:
                print('WRONG TOKEN')
                return make_response('wrong token', 403)
        else:
            return make_response('invalid params', 400)
    return 'parsing of JSON still under construction'

###################################################################

#TODO route based on SEND APIs
