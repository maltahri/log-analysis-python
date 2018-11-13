# Logs Analysis

# Introduction

###In this project, need to make one python program using query and python. The database is provided by Udacity. This program should give output below:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    Example:
    
    "Princess Shellfish Marries Prince Handsome" — 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    "Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

    Example:
    
    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

To build the reporting tool, you'll need to load the site's data into your local database.

Dowanload the newsdata.sql from Udacity. 

This is the command to configure database psql -d news -f newsdata.sql.

Run the program(Script):

python log_analysis.py

The output is shown in output.txt.
