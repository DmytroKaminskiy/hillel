import random
import string

from flask import Flask

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
    return ''.join(
        random.choice(string.ascii_uppercase) for i in range(10)
    )


@app.route('/req-txt')
def req_txt():
    return read_requirements()


@app.route('/all-customers')
def all_customers():
    from flask import request
    query = f'SELECT * FROM customers WHERE Country = \'{request.args["Country"]}\';'
    result = exec_query(query)
    return str(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
