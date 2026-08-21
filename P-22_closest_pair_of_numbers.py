''' Program 22: Write a Python program to find the closest pair of numbers (the pair with the 
smallest difference) from a comma-separated list of numbers provided by the user. '''


n = int(input("Enter a number of elements you want in your list:"))

list = []
for i in range(n):
    list.append(int(input("Enter the element : ")))

list = sorted(list)
min_def = [list[1] - list[0]]
pair = [list[0],list[1]]
for i in range(1,len(list)-1):
    if list[i+1] - list[i] < min(min_def):
        pair = [list[i],list[i+1]]

print(list)
print(pair)
    