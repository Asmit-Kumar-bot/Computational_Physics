import numpy as np

def jacobi_method(A, b, tol=1e-6, max_iterations=100):
    n = len(b)
    x = np.zeros(n)  # Initial guess
    x_new = np.zeros(n)

    for iteration in range(max_iterations):
        for i in range(n):
            sum_terms = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_terms) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1

        x[:] = x_new

    raise ValueError("Jacobi method did not converge")

def gauss_seidel_method(A, b, tol=1e-6, max_iterations=100):
    n = len(b)
    x = np.zeros(n)  # Initial guess

    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum_terms = sum(A[i, j] * x_new[j] for j in range(i)) + sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_terms) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1

        x[:] = x_new

    raise ValueError("Gauss-Seidel method did not converge")

# Input matrix and vector
A = np.array([[4, -1, 1], [2, 5, -1], [-1, 1, 4]], dtype=float)
b = np.array([3, 1, 2], dtype=float)

# Solve using Jacobi Method
jacobi_solution, jacobi_iterations = jacobi_method(A, b)
print("Jacobi Method Solution:", jacobi_solution)
print("Jacobi Method Iterations:", jacobi_iterations)

# Solve using Gauss-Seidel Method
gauss_seidel_solution, gauss_seidel_iterations = gauss_seidel_method(A, b)
print("Gauss-Seidel Method Solution:", gauss_seidel_solution)
print("Gauss-Seidel Method Iterations:", gauss_seidel_iterations)
