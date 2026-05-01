import numpy as np

def linear_solver(a_int,b_int,n):
    aug = []
    for i,k in enumerate(a_int):
        for a,b in enumerate(k):
            A[i][a]= float(b)
    for i,j in enumerate(A):
        row = A[i]
        row.append(float(b_int[i]))
        aug.append(row)
    aug = np.array(aug)
    print(aug)
    c = 0
    while c < n:  #iteratively make row have leading 1
        r = c
        if abs(aug[r][c])==0.:

            c = c+1
        else:
            temp = aug[c]
            subtractor = temp / aug[c][c]
            aug[c] = subtractor
            while r<n and r>=c:
                aug[r+1] = aug[r+1] - (aug[r+1][c]) * subtractor
                r = r + 1
            c = c+1
    #print(aug)
    val = 0
    for row in aug:
        condition = True # matrix coefficients of row = 0
        for i in row[:-1]:
            if i != 0:
                condition = False
        if condition:
            if row[-1] == 0:
                val = 1
            else:
                val = -1
    return val,aug

N = 4
A = [
    [1,5,2,3,1],
    [2,13,7,1,5],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [3,2,4,6,1]
]
b = [1,0,2,2,1]

num,aug = linear_solver(A,b,N)
for i in aug:
    for j in i:
        print(int(j*100)/100," " ,end = ",")
    print()

if num == 0:
    print("A has a unique solution")
if num == 1:
    print("A has infinite solutions")
if num == -1:
    print("A has no solutions")

# num = 0 : 1 solution
# num = 1 : infinite solution
# num = -1 : no solution


 # for c in range(n+1):
       # temp = aug[c]
      #  subtractor = temp / aug[c][c]
     #   aug[c] = subtractor
     #   for r in range(c,n):
            # loop will not be entered if i==n
       #     aug[r+1] = aug[r+1]-(aug[r+1][c])*subtractor