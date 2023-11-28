#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
"""import flask"""


from flask import Flask

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
    """ display “C ” followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    """main function"""
    app.run(host='0.0.0.0', port=5000)
