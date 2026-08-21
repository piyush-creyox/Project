''' Write a Python program to filter a list of numbers by keeping 
only the elements located at odd indices.'''
n = int(input("Enter no of element you want to enter:"))
list1=[]
for i in range(n):
    a=int(input(f"Enter element no {i+1}:"))
    list1.append(a)

list2=[]
for i in range(1,(n+1)):
    if i%2!=0:
        list2.append(list1[i-1])
print("The elements located at odd indices are:",list2)