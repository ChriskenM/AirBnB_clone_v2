#!/usr/bin/python3
"""
Script to start a Flask web application with specific routes.
"""
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """
    display a HTML page only if n is an integer
    """
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numOddEven(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
