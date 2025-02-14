import numpy as np

A = np.array([[4, -1, 1], [2, 2, 3], [5, -2, 6]], dtype=float)
b = np.array([-5, 10, 1], dtype=float)


# Apply Gauss Elimination method 
for i in range(1,3,1):
    r=i

    for k in range(i):
        
        f=A[r,k]/A[k,k]

        b[r]=b[r]-f*b[k]

        for m in range(0,3,1):
            A[r,m]=A[r,m]-f*A[k,m]
        

        
x = np.zeros(3)
x[2] = b[2] / A[2, 2]  # Solve for x3
x[1] = (b[1] - A[1, 2] * x[2]) / A[1, 1]  # Solve for x2
x[0] = (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2]) / A[0, 0]  # Solve for x1

         
print(x)

