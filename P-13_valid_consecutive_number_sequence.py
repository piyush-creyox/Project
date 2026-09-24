'''Program 13: Write a Python program to check if a sequence of numbers entered by a user 
forms a valid consecutive number sequence. The sequence must have a length between 3 and 13.'''

num = list(map(int,input("Enter a sequence of numbers seprated by space :").split()))
length = len(num)
if length >3 and length <13:
    for i in range(length-1):
        if num[i]+1 != num[i+1]:
            print("The sequence is invalid")
            break
    else:
        print("The sequence is valid")
else:
    print("The length of the sequence is not valid")
