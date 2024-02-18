#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Returns a string at the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns a string at the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """Returns a string at the /c route."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """Returns a string at the /python route."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """Returns a string at the /number route."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:number>')
def number_template(number):
    """Returns a string at the /number_template route."""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>')
def number_odd_or_even(number):
    """Returns a string at the /number_odd_or_even route."""
    status = 'even' if number % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=number, status=status)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
