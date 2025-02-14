import numpy as np

# Constructing the function
def power_iteration(A, num_iterations=100):
    # Randomly initialize a vector
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_iterations):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = b_k1 / np.linalg.norm(b_k1)
        eigenvalue = np.dot(b_k1_norm.T, np.dot(A, b_k1_norm))     
        b_k = b_k1_norm
    
    return eigenvalue, b_k

def find_eigenvalues_eigenvectors(A, k=3):
    eigenvalues = []
    eigenvectors = []
    
    A_copy = A.copy()
    
    for _ in range(k):
        eigenvalue, eigenvector = power_iteration(A_copy)
        
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)
    
        A_copy -= eigenvalue * np.outer(eigenvector, eigenvector)
    
    return eigenvalues, eigenvectors

# Implementing the function
A = np.array([[4, -2, 1],
              [1, 1, -1],
              [3, -2, 2]], dtype=float)

eigenvalues, eigenvectors = find_eigenvalues_eigenvectors(A)

print("Eigenvalues:")
for i, ev in enumerate(eigenvalues, 1):
    print(f"λ{i} = {ev:.4f}")

print("\nCorresponding Eigenvectors:")
for i, vec in enumerate(eigenvectors, 1):
    print(f"v{i} = {vec}")