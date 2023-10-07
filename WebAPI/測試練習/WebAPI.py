import flask
from flask import jsonify, render_template, request
import pandas as pd
import numpy as np

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"

@app.route('/post', methods=['POST'])
def post():
    token = request.headers['token']
    if request.headers['token'] == '123456':
        test1 = request.values['test1']
        return test1
    else:
        return '請輸入正確的token'

@app.route('/get', methods=['GET'])
def get():
    token = request.args['token']
    if request.args['token'] == '123456':
        test1 = request.args['test1']
        return "<h1>"+test1+"</h1>"
    else:
        return '<h1>請輸入正確的token</h1>'


app.run(host='192.168.50.151',port=5000)