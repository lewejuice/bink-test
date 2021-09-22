import os
import csv
from flask import Flask, render_template, flash, \
    redirect, session, url_for, request

app = Flask(__name__)

@app.route('/')
# Takes user to the home-page
@app.route('/home')
def home():
    csvfile = open('csv/test-dataset.csv','r', newline='')
    obj = csv.reader(csvfile)
    for row in obj:
        print (row)
    return render_template("index.html")

@app.route('/current_rent')
def current_rent():
    # Current rent button which displays current rent data and prints first five to the console
    return render_template("current-rent.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            debug=True)
