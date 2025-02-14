import numpy as np

# Lagrange interpolation function

def lagrange_interpolation(A, x,f):
    x_values = A[0]  
    y_values = A[1]  

    
    n = 2
    
    
    for n in range(2,4):

        result = 0

        for i in range(n):
            term = y_values[i]
            for j in range(n):
                if i != j:
                    term *= (x - x_values[j]) / (x_values[i] - x_values[j])
            result += term
        f[n-2] = result
         
 



A = np.array([
    [1, 4, 6],   
    [0, 1.3863, 1.7918]     
])

f=np.zeros(2)

x = 2  

# Lagrange Interpolation result
lagrange_interpolation(A, x,f)
print("the value of function at x = 2 by first order polynomial is ==",f[0])
print("the value of function at x = 2 by second order polynomial is ==",f[1])

