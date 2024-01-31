c = [2, 1]
A = [[1, 1],
     [1, 2],
     [1, 0]]
b = [3, 5, 2]
n=len(A[0])
m=len(A)
print(m,n)
for i in range (m):
    for j in range (n,n+m):
        if i==(j-n):
            A[i].append(1)
        else:
            A[i].append(0)
for i in range (n,n+m):
    c.append(0)
print("Matrix A in std form")
for i in range (m):
    print(A[i])
print(c)
