#!/usr/bin/python3
"""
This is a script to start a Flask web application
"""


from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def states_list():
    # This function returns a list of states
    state_v = storage.all(State)
    amenity = storage.all(Amenity)
    places = storage.all(Place)
    state_v = sorted(state_v.values(), key=lambda state: state.name)
    amenity = sorted(amenity.values(), key=lambda resource: resource.name)
    places = sorted(places.values(), key=lambda resource: resource.name)
    data = [state_v, amenity, places]
    return render_template('100-hbnb.html', data=data)


@app.teardown_appcontext
def teardown_app(args=None):
    # This closes down the session
    storage.close()


if __name__ == "__main__":
    # This makes the app run of host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
