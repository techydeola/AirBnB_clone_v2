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


@app.route('/c/')
@app.route('/c/<text>', strict_slashes=False)
def cDisplay(text='is cool'):
    """
        This functions handles the C view
    """
    if '_' in text:
        newtext = text.replace('_', ' ')
        return "python {}".format(newtext)
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyDisplay(text='is cool'):
    """
        This function handles the python display
    """
    if '_' in text:
        newtext = text.replace('_', ' ')
        return "python {}".format(newtext)
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
