#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id=None):
    """ Function called with /states route """
    states = storage.all(State)

    if not id:
        sorted_states = sorted(states.values(), key=lambda x: x.name)
        states_dict = {state.id: state for state in sorted_states}
        return render_template('9-states.html',
                               Table="States",
                               states=states_dict)

    k = "State.{}".format(id)
    if k in states:
        cities = sorted(states[k].cities, key=lambda x: x.name)
        return render_template('9-states.html',
                               Table="State: {}".format(states[k].name),
                               states={k: states[k]},  # Pass as a dictionary
                               cities=cities)

    return render_template('9-states.html', states=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
