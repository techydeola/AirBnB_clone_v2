#!/usr/bin/python3
""" This module is a scripts that starts a flask web app """


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """ This function handles closing of the db """
    storage.close()


@app.route('/states_list')
def state():
    """ This function parses the state objects """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
