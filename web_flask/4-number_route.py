#!/usr/bin/python3
""" This is a flask app module """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        This function handles the home view
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        This function handles the HBNB view
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cDisplay(text):
    """
        This functions handles the C view
    """
    newtext = text.replace('_', ' ')
    return "python {}".format(newtext)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyDisplay(text='is cool'):
    """
        This function handles the python display
    """
    newtext = text.replace('_', ' ')
    return "python {}".format(newtext)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This function handles the 'number' view """
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
