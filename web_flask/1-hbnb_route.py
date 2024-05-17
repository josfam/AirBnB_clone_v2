#!/usr/bin/python3

"""A Flask web application for the airbnb clone application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The default home route when visiting the site"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """For the /hbnb route on the site"""
    return 'HBNB'


app.run(host='0.0.0.0', port=5000)
