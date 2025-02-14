import numpy as np

def faddeev_leverrier(matrix):
    n = len(matrix)
    A = np.array(matrix, dtype=float)
    I = np.eye(n)
    B = A.copy()
    traces = []
    
    # Compute traces and update B
    for k in range(1, n + 1):
        trace = np.trace(B) / k
        traces.append(trace)
        B = A @ (B - trace * I)
    
    # Characteristic polynomial coefficients (from traces)
    coeffs = [(-1)**k * traces[k] for k in range(n)]
    coeffs.insert(0, (-1)**n)  # Leading coefficient
    
    # Find eigenvalues (roots of the characteristic polynomial)
    eigenvalues = np.roots(coeffs[::-1])  # Reverse for np.roots
    
    # Find eigenvectors
    eigenvectors = []
    for eigenvalue in eigenvalues:
        # Solve (A - eigenvalue * I) * v = 0
        M = A - eigenvalue * I
        _, _, V = np.linalg.svd(M)  # Singular value decomposition
        eigenvector = V[-1]  # Last row of V is the eigenvector
        eigenvectors.append(eigenvector)
    
    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    # Input matrix
    matrix = [
    [0,1,0],
    [0,0,1],
    [2,-5,4]
]

    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = faddeev_leverrier(matrix)
    
    # Print results
    print("Eigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    for i, eigenvector in enumerate(eigenvectors):
        print(f"Eigenvector for eigenvalue {eigenvalues[i]}:")
        print(eigenvector)