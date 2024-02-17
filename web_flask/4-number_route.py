#!/usr/bin/python3
"""
Script to start a Flask web application with specific routes.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    function displays text
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    function returns text
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """
    display “C ” followed by the value of the text
    """
    result = text.replace('_', ' ')
    return 'C {}'.format(result)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Py_print(text='is cool'):
    """
    display "Python" followed by value of text
    """
    result = text.replace('_', ' ')
    return 'Python {}'.format(result)


@app.route('/number/<int:n>', strict_slashes=False)
def number_print(n):
    """
    display “n is a number” only if n is an integer
    """
    if type(n) == int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
