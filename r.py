import numpy as np

def faddeev_leverrier(matrix):
    n = matrix.shape[0]
    A = np.array(matrix, dtype=float)
    
    # Initialize variables
    P_prev = A.copy()
    coefficients = []
    
    for k in range(1, n + 1):
        trace = np.trace(P_prev)
        c_k = -trace / k
        coefficients.append(c_k)
        
        # Compute P_k
        if k < n:
            P_prev = A @ P_prev + c_k * np.eye(n)
    
    # The constant term c_0 is det(A) / (-1)^n
    c_0 = (-1)**n * np.linalg.det(A)
    coefficients.append(c_0)
    
    return coefficients

def eigenvalues_and_eigenvectors(matrix):
    # Get coefficients of characteristic polynomial
    coefficients = faddeev_leverrier(matrix)
    
    # Characteristic polynomial
    print("Characteristic Polynomial Coefficients:", coefficients)
    
    # Solve for eigenvalues
    roots = np.roots(coefficients)
    print("Eigenvalues:", roots)
    
    # Find eigenvectors
    eigenvectors = []
    for eigenvalue in roots:
        eigenvector = null_space(matrix - eigenvalue * np.eye(matrix.shape[0]))
        eigenvectors.append(eigenvector)
        
    return roots, eigenvectors

def null_space(A, tol=1e-9):
    """Compute the null space of a matrix."""
    u, s, vh = np.linalg.svd(A)
    null_mask = (s <= tol)
    null_space = np.compress(null_mask, vh, axis=0)
    return null_space.T

# Given Matrix
A = np.array([
    [4, -2, 1],
    [1, 1, -1],
    [3, -2, 2]
])

# Compute eigenvalues and eigenvectors using Faddeev-Leverrier
roots, eigenvectors = eigenvalues_and_eigenvectors(A)
print("\nEigenvalues:", roots)
print("Eigenvectors:", eigenvectors)
