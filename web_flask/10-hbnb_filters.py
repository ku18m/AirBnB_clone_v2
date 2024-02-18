#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the current sqlalchemy session."""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Returns a string at the /hbnb_filters route."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
