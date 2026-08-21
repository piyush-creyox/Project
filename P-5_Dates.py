''' Write a Python program that accepts three dates from the user (in YYYY-MM-DD format) 
and checks whether the third date falls chronologically between the first two dates.'''

date1 = input("Enter Date in \" YYYY-MM-DD\" format :")
date2 = input("Enter Date in \" YYYY-MM-DD\" format :")
date3 = input("Enter Date in \" YYYY-MM-DD\" format :")

if date1 < date3 < date2:
    print("Date 3 is between Date 1 and Date 2.")
else:
    print("Date 3 is not in between Date 1 and Date 2.")