#!/usr/bin/python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
Flask application with dynamic content using Jinja loops and conditions
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    """Route to display items from JSON file"""
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



