import numpy as np

# Define the matrix
A = np.array([[2, 1, 3],
              [1, 2, 1],
              [3, 1, 2]], dtype=float)

B = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]], dtype=float)


a = np.hstack((A, B.reshape(3, 3)))


def inverse_matrix(z):
    for i in range(0,3):
        a[i] = a[i]/a[i,i]

        for j in range(0,3):
        
            if i != j:
                f=a[j,i]
                a[j] = a[j]-f*a[i]

    return(a[:, 3:])



print(inverse_matrix(a))
