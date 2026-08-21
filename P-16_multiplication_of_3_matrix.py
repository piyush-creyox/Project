'''Program 16: Write a Python program to perform Matrix Multiplication on an M x N matrix 
and an N x P matrix.'''
M = int(input("Enter number of elements in M : "))
N = int(input("Enter number of elements in N : "))
P = int(input("Enter number of elements in P : "))
mat1_size = M*N
mat2_size = N*P
mat1 = []
mat2 = []
mat3 = [[0 for _ in range(P)] for _ in range(M)]

for i in range(M):
    lst1 = []
    for j in range(N):
        lst1.append(int(input("Enter element of mat1 : ")))
    mat1.append(lst1)
for i in range(N):
    lst2 = []
    for j in range(P):
        lst2.append(int(input("Enter element of mat2 : ")))
    mat2.append(lst2)

for i in range(M):
    for j in range(P):
        for k in range(N):
            mat3[i][j] = mat3[i][j]+(mat1[i][k]* mat2[k][j])

print(mat3)

        
