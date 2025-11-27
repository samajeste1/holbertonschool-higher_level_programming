#!/usr/bin/python3
"""
Task 1: Creating a Basic HTML Template in Flask
Basic Flask application with Jinja templates
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home route"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About route"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact route"""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)



