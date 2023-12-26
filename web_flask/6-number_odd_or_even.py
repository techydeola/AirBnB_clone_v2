#!/usr/bin/python3
""" This is a flask app module """


from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if (n % 2) == 0:
        return render_template('6-number_odd_or_even.html',
                               num=n, num_type='even')
    if (n % 2) != 0:
        return render_template('6-number_odd_or_even.html',
                               num=n, num_type='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
