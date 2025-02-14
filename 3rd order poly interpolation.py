import numpy as np




def coefficent(A):
    x = A[0]
    y = A[1]
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
     
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef[0]
    


def interpolation(A,  coef, x_1):

    x = A[0]
    n = len(x)
    result = 0
    for i in range(n):
        term = coef[i]

        for k in range(0,i):
            term = term*(x_1-x[k])

        result =result+term
    
    return result



A = np.array([
    [1, 4, 5, 6],
    [0, 1.3863, 1.6094, 1.7918]
])

x_1=2

coef = coefficent(A)

print(coef)

print(interpolation(A,  coef, x_1))