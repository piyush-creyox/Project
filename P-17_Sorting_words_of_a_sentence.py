'''Program 17: Write a Python program that accepts a sentence from the user, splits it into words, 
sorts the words alphabetically, and prints them separated by commas.'''


sentence = input("Enter sentence : ").lower().split()
print(sentence)
sorted_sentence = sorted(sentence)
print(",".join(sorted_sentence))

