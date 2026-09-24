'''Program 27: Write a Python program that takes a comma-separated list of
numbers as input from the user and uses list comprehension to print the 
square of each odd number in the list.'''



number = input("Enter numbers with comma separated :")
number = number.split(",")
number = list(map(int,number))

squre = [num**2 for num in number if num%2 != 0] 
print(squre)