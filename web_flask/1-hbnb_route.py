#!/usr/bin/python3
""" This is a flask module """


from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
        This function defines the view for the '/hbnb' url
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
