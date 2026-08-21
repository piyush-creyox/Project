#Write a Python program to add three predefined 3x3 matrices together and print the resulting matrix.
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[9,8,7],[6,5,4],[3,2,1]]
matrix3=[[4,5,6],[7,8,9],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j]=matrix1[i][j]+matrix2[i][j]+matrix3[i][j]
    
print("The sum of the matrices is: ",result)