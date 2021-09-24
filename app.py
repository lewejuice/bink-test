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
        for x in sort:
            # Makes sure the line is not a field and makesure it doesn't go over 5 lines
            if x is not fields and count < 5:
                count += 1
                print(x)

        return render_template("current-rent.html")

"""
Creates a new list of mast data which
all have 25 lease years.
"""
@app.route('/lease_years')
def lease_years():
    # csv file name
    filename = 'csv/test-dataset.csv'
    
    # initializing the rows list
    rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a data object
        data = csv.reader(csvfile, delimiter = ',')
        fields = next(data)
        total_rent = []

        for x in data:
            if x[-2] == '25':
                rows.append(x)
                # Works out the total rent for all items in the list
                total_rent.append(+int(float(x[-1])) * 25)
        
        print(rows)
        print('Total ammount of rent for each 25 year lease:')
        print(total_rent)
        return render_template("lease-years.html")

"""
Creates a dictionary of the tenants name
and how many masts that tenant holds.
"""
@app.route('/tenant')
def tenant():
    # csv file name
    filename = 'csv/test-dataset.csv'
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a data object
        data = csv.reader(csvfile, delimiter = ',')
        # Defines the fields
        fields = next(data)

        # Defines empty list of tenants
        tenants = []

        # Retrieve each tenants name and split string into two list items at ampersands, then append to list.
        for eachline in data:
            if eachline is not fields:
                split_tenants = eachline[6].split('&')
                tenants.append(split_tenants)
        
        # Join sub lists into one list of tenants names.
        cleaned_tenants = list(itertools.chain.from_iterable(tenants))

        # Function to remove full stops from strings.
        def remove_fullstop(string):
            punc = '.'
            for ele in string:
                if ele in punc:
                    string = string.replace(ele, '')
            return string

        # Pass data through the function to remove full stops.
        tenants = [remove_fullstop(i) for i in cleaned_tenants]

        # Count how many times each name is repeated in the list and put it into a dictionary
        tenant_dict = {i:tenants.count(i) for i in tenants}

        print(tenant_dict)

        return render_template("tenant.html")

"""
Creates a list of all the rentals with a start
lease date between 1st June 1999 and 31st August
2007 and changes the formatting of the dates.
"""
@app.route('/lease_start')
def lease_start():
    # csv file name
    filename = 'csv/test-dataset.csv'
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a data object
        data = csv.reader(csvfile, delimiter = ',')
        
        # Defines the fields
        fields = next(data)

        # Star date and end date
        sdate = date(1999, 6, 1)
        edate = date(2007, 8, 31)

        # For loop to iterate through the data
        for eachline in data:
            # Change the format of the dates in each line of data
            date_set = datetime.strptime(eachline[7], '%d %b %Y')
            end_date_set = datetime.strptime(eachline[8], '%d %b %Y')
            # filters for dates between the start and end date
            if sdate <= datetime.date(date_set) and datetime.date(date_set) <= edate:
                # Reformats the dates to display day-month-year
                eachline[7] = datetime.strftime(date_set, '%d-%m-%Y')
                eachline[8] = datetime.strftime(end_date_set, '%d-%m-%Y')
                print(eachline)

        return render_template("lease-start.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            debug=True)
