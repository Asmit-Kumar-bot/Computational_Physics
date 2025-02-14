import numpy as np

# Lagrange interpolation function
def lagrange_interpolation(A, x):
    x_values = A[0]  
    y_values = A[1]  

    
    n = len(x_values)
    result = 0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result
 



A = np.array([
    [1.2, 1.3, 1.4, 1.5],   
    [1.063, 1.091, 1.119, 1.145]     
])

x = 1.35  

# Lagrange Interpolation result
print("the value of function at x = 1.35 is ---",lagrange_interpolation(A, x))
