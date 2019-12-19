import random
import string

from flask import Flask, request

from db import exec_query
from utils import read_requirements

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello'


@app.route('/hello-world')
def hello_world():
    for i in range(100):
        return str(i)


@app.route('/gen')
def gen():
    number = int(request.args['number'])
    # if number not in range(100):
    #     return 'Wrong number'
    if 0 < number < 100:
        return ''.join(
            random.choice(string.ascii_uppercase) for _ in range(10)
        )
    return 'Wrong number'


@app.route('/req-txt')
def req_txt():
    return read_requirements()


@app.route('/all-customers')
def all_customers():
    query = f'SELECT * FROM customers WHERE Country = \'{request.args["Country"]}\';'
    result = exec_query(query)
    return str(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
