# Bink Test

This project is a technical test provided by Bink.

## How I found the test

I found some aspects of the test very challenging as most of it was new to me. I had to overcome these problems through research and self learning.
Here are my problems and solutions
:

```bash
1. Problem - I had never opened a CSV file with python, which was needed to complete all tasks.
```
Solution - I found useful documentation online on how to do this, which ended up being very simple with the built in CSV module in python.
```bash
2. Problem - Task 1 had one bug where I first tried using operator.itemgetter(), 
it seemed to put them in all order apart from the first two.
```
Solution - I fixed this issue by using lambda, but I had to first turn the strings into integers and float the value to nearest whole number for it work.
```bash
3. Problem - I found task 2 the simplest of the four, but the question slightly
puzzled me on wether I should add up each current rent in the list or multiply
each current by the 25 year lease.
```
Solution - I decided to go with adding them up which was an easy fix.
```
4. Problem - I probably found task 3 the most challenging (which I really enjoyed).
The two main issues were there being a full stop in one of the names but mainly allot of
masts had a shared tenancy between two companies.
```
Solution - Firstly I had to split all the tenants at each ampersand, which then left me with two names split but inside their own individual lists, which confused things further. So I then did some research into splitting lists up or merging them together, which lead me to itertools. This gave me away of merging all the separate lists into one single list of names. Secondly I built a separate function to erase the full stops, and then simply passing the data through the function.
```bash
5. Problem - Task 4 I was slightly more familiar with, but definitely still a challenge.
I had a problem with passing a certain date format and changing it to one which could then be queried.
```
Solution - With research I found two very useful tools in the datetime module. Firstly strptime, which reformatted the original data (21 Aug 2007) to (2007-08-21). I could then use this to find which dates fell between the two dates provided, I then used strftime to reformat the dates again to the required format (21-08-2007).

## Automated Testing

I wrote a series of automated testing to make sure there were no bugs or errors. I had never built automated testing using the Flask framework, but I found all the documentation I needed online.

Tests:

1. I first tested to see if the flask application was up running properly by checking the status code was equal to 200, but also checking the right html text was being loaded also.

2. Next I tested the task 1 function was working correctly and wasn't throwing any errors and also printed the results to the console.

3. Next I tested the task 2 function was working correctly and wasn't throwing any errors and also printed the results to the console.

4. Next I tested the task 3 function was working correctly and wasn't throwing any errors and also printed the results to the console.

5. Next I tested the task 4 function was working correctly and wasn't throwing any errors and also printed the results to the console.

## Technologies Used

1. HTML - Used to render web pages with buttons to run each function.
2. Python - Used to built the main application and write the functions for each task.
3. Flask - The web framework I used to help build the web application.

## Disclosure
This project was built for the sole purpose of a technical test for Bink.