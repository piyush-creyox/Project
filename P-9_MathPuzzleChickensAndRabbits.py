'''Write a Python program to solve the "Chickens and Rabbits" math 
puzzle: Given the total number of heads (e.g., 35) and total legs 
(e.g., 94), calculate how many chickens and rabbits there are.'''

heads = int(input("Enter no of heads:"))
legs = int(input("Enter no of legs:"))


Chickens_lag = heads * 2
Rabbits =  (legs - Chickens_lag)//2
Chickens = heads - Rabbits
print("No of chickens:",Chickens)
print("No of Rabbits:",Rabbits)