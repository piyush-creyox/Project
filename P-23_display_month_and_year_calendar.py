'''Program 23: Write a Python program to print the calendar for a specific month and year 
(e.g., November 2014) using Python's built-in calendar module.'''

import calendar

y = int(input("Enter a year : "))
m = int(input("Enter a month : "))
print(calendar.month(y,m))

