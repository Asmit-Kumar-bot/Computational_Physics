import numpy as np

# Find the value of square root of 2 by liner interpolation

def linear_interpolation(A,x):
    result = A[1][0] + (x - A[0][0])*(A[1][1] - A[1][0])/(A[0][1] - A[0][0])  

    return result








A = np.array([
    [1, 4, 9, 16],
    [1, 2, 3, 4]
])
x=6

print(linear_interpolation(A,x))