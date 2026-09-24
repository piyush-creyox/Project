''' Write a Python program that accepts a sentence as input and counts the frequency of each word
within the sentence. '''

word=input("Enter Sentence :").lower().split()

result = {}
for i in range(len(word)):
    if word[i] in result.keys():
        result[word[i]] += 1
        
    else:
        result[word[i]] = 1
print("\nFrequency of each word is :",result)
