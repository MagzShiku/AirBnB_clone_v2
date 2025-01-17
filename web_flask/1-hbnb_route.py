#!/usr/bin/python3
"""a script that starts a Flask web application:"""


from flask import Flask
"""import Flask from falsk"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return string 1"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return string 2"""
    return 'HBNB'


if __name__ == '__main__':
    """main function"""
    """run at the 0.0.0.0, & 5000 port"""
    app.run(host='0.0.0.0', port=5000)
