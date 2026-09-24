'''Write a Python program to take two lists—one with integer keys and one with string 
values—pair them together, and sort the pairs based on the values in the integer list. '''

list1 = [2,1,3,5]
list2 = ["Rajkot", "surat" , "Jamnagar", "Ahmedabad"]

dict1 = dict(zip(list1, list2))

sorted_dict = dict(sorted(dict1.items()))
print("Sorted Dictionary is :", sorted_dict)

# Another Method
dict2 = {}
for i in range(len(list1)):
    dict2[list1[i]] = list2[i]
print("\nDictionary is :",dict2)
