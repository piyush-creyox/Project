'''Program 15: Write a Python program to filter and print the odd numbers from a list of 
integers from 1 to 15 using the filter() function alongside a lambda expression.'''



odd_numbers = filter(lambda x: x % 2 != 0, range(1,16))
print(list(odd_numbers))