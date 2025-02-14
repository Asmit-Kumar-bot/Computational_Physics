import numpy as np

# Linear interpolation function
def linear_interpolation(A, r):
    x = A[0]  
    y = A[1]  

    
    for i in range(len(x) - 1):
        if x[i] <= r <= x[i + 1]:
            
            result = y[i] + (r - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            return result
    
    return None  



A = np.array([
    [1, 4, 9, 16],   
    [1, 2, 3, 4]     
])

r = 2  # Find sqrt(2)

# Linear Interpolation result
print(linear_interpolation(A, r))
