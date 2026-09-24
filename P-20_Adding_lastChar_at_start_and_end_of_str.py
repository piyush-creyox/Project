'''Program 20: Write a Python program to create a new string where the last character 
of a given string is attached to both its front and back.'''



inp = input("Enter string :")
print("original str is :" , inp)
last_char = len(inp)-1
print("Last char is : ",inp[last_char])
new_str = inp[last_char] + inp + inp[last_char]
print("The new str is : ", new_str)
