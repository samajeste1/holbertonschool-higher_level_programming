#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
Flask application that reads and displays product data from JSON or CSV files
"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data(product_id=None):
    """Read data from JSON file"""
    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
            if product_id:
                for product in products:
                    if product.get('id') == int(product_id):
                        return [product]
                return None
            return products
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_data(product_id=None):
    """Read data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if product_id and int(row['id']) == int(product_id):
                    return [row]
                products.append(row)
        if product_id:
            return None
        return products
    except FileNotFoundError:
        return None
    except Exception:
        return None


@app.route('/products')
def products():
    """Route to display products from JSON or CSV"""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source == 'json':
        products_data = read_json_data(product_id)
    elif source == 'csv':
        products_data = read_csv_data(product_id)
    else:
        return render_template('product_display.html', error='Wrong source')

    if products_data is None:
        return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products_data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



