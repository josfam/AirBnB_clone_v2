#!/usr/bin/python3

"""A Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The home route"""
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=5001)
