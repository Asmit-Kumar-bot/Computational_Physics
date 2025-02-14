import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    # Augment matrix
    a = np.hstack((A, b.reshape(-1, 1)))

    # Apply Gauss-Jordan elimination
    for i in range(n):
        # Make the diagonal element 1
        a[i] = a[i] / a[i, i]
        for j in range(n):
            if i != j:
                f = a[j, i]
                a[j] -= f * a[i]

    # Extract sol
    return a[:, -1]

# Input system
A = np.array([[2, 1, 1],            #2x+y+z=10
                [3, 2, 3],          #3x+2y+3z=18
                 [1, 4, 9]          #x+4y+8z=16
                 ], dtype=float)
b = np.array([10, 18, 16], dtype=float)

# Solve using Gauss-Jordan Method
sol = gauss_jordan(A, b)
print(sol)
