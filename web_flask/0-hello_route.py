#!/usr/bin/python3
"""Flask app that returns a string at the root route."""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string at the root route."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
