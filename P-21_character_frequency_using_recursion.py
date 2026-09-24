'''Program 21: Write a Python program using recursion to count the frequency of each 
individual character in an input string.'''
 

def character_freq(string1, freq=None):

    if freq is None:
        freq = {}
   
    if string1 == "":
        return freq
   
    char = string1[0]
    
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
  
    return character_freq(string1[1:], freq)

str1 = input("Enter String: ")

result = character_freq(str1)

print(result)