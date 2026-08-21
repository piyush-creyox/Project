''' Program 25: Write a Python program that takes a sentence as input and iterates over it to 
count the total number of upper-case letters and lower-case letters.'''

string1 = input("Enter the string:")
upper_count = 0
lower_count = 0
for char in string1:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count+= 1

print("the no. of upper case letters is :", upper_count)
print("the no. of lower case letters is :", lower_count)
            
