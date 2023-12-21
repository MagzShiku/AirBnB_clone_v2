#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
"""import Flask"""

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """return the string ('Hello HBNB!)"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """main caller"""
    app.run(host='0.0.0.0', port=5000)
