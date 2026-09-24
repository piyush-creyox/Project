'''Program 18: Write a Python program that continuously accepts numbers from the user until 
they type 'q'. Once stopped, it should calculate and print: the minimum, the maximum, 
the total sum, the average, the number with the longest digit length, and the pair of numbers 
with the smallest mathematical difference.'''
import math
num = []

while True:
    a = input("Eneter q to quite. : ").lower()
    if a == 'q':
        break
    else:
        num.append(int(a))

#Min and Max
print("Min : ", min(num))
print("Max : ", max(num))

# Total sum
print("Sum :", sum(num))

#Avg.
print("Avg :", sum(num)/len(num))

#No with longest digit length
max_len = 0
num1 = num[0]
for i in range(1,len(num)):
    digit_len = len(str(num[i]))
    if digit_len > max_len:
        max_len = digit_len
        num1 = num[i]

print("Number with longest digit length :", num1)

# No. with the smallest mathematical difference.
smallest_diff = sorted(num)
min = smallest_diff[1] - smallest_diff[0]
pair=[smallest_diff[0], smallest_diff[1]]

for i in range(1,len(smallest_diff)-1):
    min_diff = smallest_diff[i+1] - smallest_diff[i]
    if min_diff < min:
        min=min_diff
        pair=[smallest_diff[i],smallest_diff[i+1]]

print("Pair with smallest difference :", pair) 
    

    