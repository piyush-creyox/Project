'''Program 24: Write a Python program that accepts a comma-separated list of values. 
Check if each value is exactly a 4-digit binary string consisting only of 1s and 0s, and 
then print the values that are cleanly divisible by 5.'''
 

values = input("Enter values seprated by comma :")
list1= values.split(",")
temp = []
for i in range(len(list1)):
    if len(list1[i])== 4:
        temp.append(list1[i])

velid = []
for i in range(len(temp)):
    flag = 0
    for j in range(len(temp[i])):
        if temp[i][j] not in '01':
            flag = 1
            break
    if flag == 0:
        if int(temp[i],2) % 5 ==0:
            velid.append(temp[i])

print(velid)