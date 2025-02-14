import numpy as np

def gauss_elimination(T):
    n = len(T)
    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            



# Input system
A = np.array([
    [0,1,0],
    [0,0,1],
    [2,-5,4]
], dtype=float)


w = len(A)

s=2      #  eigen value put here


def eigen_vector(A,s):
    M=A-s*np.identity(w)
    return M
A=eigen_vector(A,s)
#print(A)
q=gauss_elimination(A)
print(A)



n=2

x = np.zeros(w)
for i in range(w - 1, -1, -1):
    if all(element == 0 for element in A[i]):
        x[i] = 1
    else:
        total = 0  # Renamed from 'sum' to 'total'
        for j in range(i + 1, w):
            if A[i][i] == 0:
                raise ValueError("Division by zero encountered in back substitution.")
            total += A[i][j] * x[j]
        x[i] = (0 - total) / A[i][i]  # Use 'total' instead of 'sum'
print()
print(x)