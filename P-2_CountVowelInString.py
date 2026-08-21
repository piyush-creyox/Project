'''Write a Python program to count and print the frequency of each vowel
(a, e, i, o, u) in a given multi-line string.'''

string = input("Enter String :").lower()
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
for i in range(len(string)):
    if string[i]=='a':
        count_a +=1
    elif string[i]=='e':
        count_e +=1
    elif string[i] == 'i':
        count_i +=1
    elif string[i]== 'o':
        count_o +=1
    elif string[i] == 'u':
        count_u += 1
print(f"Frequency of 'a' : {count_a}")
print(f"Frequency of 'e' : {count_e}")
print(f"Frequency of 'i' : {count_i}")
print(f"Frequency of 'o' : {count_o}")
print(f"Frequency of 'u' : {count_u}")

    