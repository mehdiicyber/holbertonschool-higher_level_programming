#!/usr/bin/python3

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def read_csv(filepath):
    products = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert ID to int and Price to float for consistency
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validation: Source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Data Loading
    try:
        if source == 'json':
            products = read_json('products.json')
        else:
            products = read_csv('products.csv')
    except Exception:
        return render_template('product_display.html', error="File not found")

    # Validation: Filter by ID
    if product_id:
        try:
            pid = int(product_id)
            products = [p for p in products if p['id'] == pid]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
