# app.py
from flask import Flask  

app = Flask(__name__)
# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return "Hello World!"

app.run(debug = True)
