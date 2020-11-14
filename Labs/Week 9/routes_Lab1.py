from flask import Flask
import math
from flask import request

app = Flask('webapp')
@app.route('/')
def home():
    return "Poverty Project"

@app.route('/sqrt/<num>')
def squared_root_num(num):
    return str(math.sqrt(int(num)))

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Nice to meet you!"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return f"this was a post with data {dict(result)}"
    else:
        return f"this was a {request.method}"

