import csv

with open('templates/Products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    with open('/templates/Products.csv', 'r') as file:
        reader = csv.reader(file)
        products = list(reader)
    return render_template('templates/index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)