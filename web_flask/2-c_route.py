#!/usr/bin/python3
""" This is a flask module """


from flask import Flask
app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def hello(text):
    """
        This function defines the view for the '/c/<text>' url
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
