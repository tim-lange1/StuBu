from flask import Flask, request
import json
import functions.math as m
import functions.login as l
app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    fulfillmentText = ''
    sum = 0
    if query_result.get('action') == 'multiply.numbers':
        return {
            "fulfillmentText": m.multiply(query_result),
            "source": "webhookdata"
        }

    if query_result.get('action') == 'input.welcome':
        set = str(l.question())
        return {set}

if __name__ == '__main__':
    app.run(port=5000) # This line is required to run Flask on repl.it