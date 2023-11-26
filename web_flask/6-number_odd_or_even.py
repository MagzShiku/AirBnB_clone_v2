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
def python_text(text='is cool'):
    # Replace underscores with spaces
    processed_text = text.replace('_', ' ')
    return 'Python {}'.format(processed_text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render an HTML page with the number
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return 'Not a valid number'


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    # Render an HTML page indicating if the number is even or odd
    if isinstance(n, int):
        return render_template('number_odd_or_even.html', number=n,
                               result='even' if n % 2 == 0 else 'odd')
    else:
        return 'Not a valid number'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
