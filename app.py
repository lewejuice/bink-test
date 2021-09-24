import os
import csv
import itertools
from datetime import datetime, date, timedelta
from flask import Flask, render_template, flash, \
    redirect, session, url_for, request

app = Flask(__name__)

@app.route('/')
# Takes user to the home-page
@app.route('/home')
def home():
    return render_template("index.html")

"""
Current rent function which displays current
rent data in order starting with the lowest
and prints first five to the console
"""
@app.route('/current_rent')
def current_rent():
    # csv file name
    filename = 'csv/test-dataset.csv'
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a data object
        data = csv.reader(csvfile, delimiter = ',')

        # Defines the fields
        fields = next(data)

        # Starting count variable
        count = 0

        # Retrieves the current rent, rounds it, turns it into a integer and then sorts it in order
        sort = sorted(data, key=lambda x : int(float(x[-1])))
        # For loop to iterate through each line
        for eachline in sort:
            # Makes sure the line is not a field and makesure it doesn't go over 5 lines
            if eachline is not fields and count < 5:
                count += 1
                print(eachline)

        return render_template("current-rent.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            debug=True)
