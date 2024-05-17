#!/usr/bin/python3

"""A Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """For /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """For /hbnb"""
    return 'HBNB'


app.run(host='0.0.0.0', port=5000)
