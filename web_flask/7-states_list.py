#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
from models import storage
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
type = os.getenv('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the current sqlalchemy session."""
    storage.close()


@app.route('/states_list')
def states_list():
    """Returns a string at the /states_list route."""
    if type == "db":
        states = storage.all("State")
    else:
        states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
