#!/usr/bin/python3
"""
This is a script to start a Flask web application
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    # This is my first flask app
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    # This route returns hbnb
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # This route returns C + text passed in URL
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text="is cool"):
    # This route returns Python + text passed in URL
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == "__main__":
    # This makes the app run of host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
