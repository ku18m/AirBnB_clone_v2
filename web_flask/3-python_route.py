#!/usr/bin/python3
"""Flask app"""
from flask import Flask


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


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
