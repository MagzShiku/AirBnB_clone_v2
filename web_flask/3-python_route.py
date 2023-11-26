#!/usr/bin/python3
"""
This is a Script that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Return HBNB
    """
    return "HBNB"


# Route: /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    processed_text = text.replace('_', ' ')
    return 'C {}'.format(processed_text)


# Route: /python/<text>
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    if "_" in text:
        p_text = text.replace("_", " ")
    else:
        p_text = text
    return f"Python {text_var}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
