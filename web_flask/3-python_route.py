#!/usr/bin/python3
"""a script that starts a Flask web application:"""

from flask import Flask
"""import module flask"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """string 1"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """string 2"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """return c"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """return python"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    """main function"""
    app.run(host='0.0.0.0', port=5000)
