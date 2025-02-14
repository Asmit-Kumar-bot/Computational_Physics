import numpy as np




def matrix_multiply(matrix1, matrix2):
    result = [[0 for _ in range(3)] for _ in range(3)]
    # Perform matrix multiplication
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def trace(matrix):

    # Calculate the trace (sum of diagonal elements)
    trace = sum(matrix[i][i] for i in range(3))
    return trace



def faddeev_leverrir(A,C_1,a,D):
    for i in range(2,4):
        C=matrix_multiply(A,C_1)-a*D
        
        a=trace(C)/i

        x[i]=a

        D=C_1
        C_1=C



def find_roots(coefficients):
    # Use numpy's roots function to find the roots of the polynomial
    roots = np.roots(coefficients)
    return roots

# Given Matrix
A = np.array([
    [4, -2, 1],
    [1, 1, -1],
    [3, -2, 2]
])
C_1 = np.array([
    [4, -2, 1],
    [1, 1, -1],
    [3, -2, 2]
])
D = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
x = np.zeros(4)

a=trace(A)
x[0]=1
x[1]=a
# Compute eigenvalues and eigenvectors using Faddeev-Leverrier\
y=faddeev_leverrir(A,C_1,a,D)
print(x)
roots=find_roots(x)
print(roots)