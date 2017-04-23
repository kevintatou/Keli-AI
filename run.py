from flask import Flask, request
import test
import json
import importlib
import tensorflow as tf
app = Flask(__name__)



sent_list = []

# gets post data and sends it to our AI to analyse
def post():
    sentiment = {"pos_or_neg": test.use_neural_network}
    name=request.get_json() 
    if request.method == 'POST':
        return json.dumps(sentiment['pos_or_neg'](name[0]['question']))

@app.route("/", methods=['POST'])
def index():
    test.reset()        # Resets our graph
    importlib.reload(test) #reloads import test
    return post()
    

if __name__ == "__main__":
    app.run(debug=True)