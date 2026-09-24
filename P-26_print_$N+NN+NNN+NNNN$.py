''' Program 26: Write a Python program that accepts an integer (e.g., $N$) and computes the value 
formula of $N + NN + NNN + NNNN$. (For example, if the input is 9, the output is calculated 
as 9 + 99 + 999 + 9999).'''


digite = int(input("Enter number : "))
sum = 0
for i in range(1,5):
    str1 = str(digite)*i
    sum = sum + int(str1)
    print(str1, end=" + ")
print("\n",sum)

