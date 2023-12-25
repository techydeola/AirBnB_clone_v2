""" This is a flask module """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        This function defines the view for the '/' url
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
