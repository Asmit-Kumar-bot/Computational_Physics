# Function to perform LU decomposition 
def lu_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # L matrix (lower triangular)
        for k in range(i, n):
            L[k][i] = matrix[k][i] - sum(L[k][j] * U[j][i] for j in range(i))

        # U matrix (upper triangular)
        for k in range(i + 1, n):
            U[i][k] = (matrix[i][k] - sum(L[i][j] * U[j][k] for j in range(i))) / L[i][i]

        L[i][i] = matrix[i][i] - sum(L[i][j] * U[j][i] for j in range(i))  # Diagonal of L
        U[i][i] = 1  # Diagonal of U is set to 1
    
    return L, U

# Function for (solve L*z = b)
def forward(L, b):
    n = len(L)
    z = [0] * n
    for i in range(n):
        z[i] = (b[i] - sum(L[i][j] * z[j] for j in range(i))) / L[i][i]
    return z

# Function for (solve U*x = z)
def backward(U, z):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = z[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))
    return x

# Coefficient matrix A and b
A = [[1, 1, 1],
     [4, 3, -1],
     [3, 5, 3]]
b = [1, 6, 4]

# Perform LU decomposition
L, U = lu_decomposition(A)

# Solve the szstem using forward and backward substitution
z = forward(L, b)
x = backward(U, z)

# Displaz results
'''
print("Lower Triangular Matrix (L):")
for row in L:
    print(row)

print("\nUpper Triangular Matrix (U) (Diagonal elements = 1):")
for row in U:
    print(row)'''

print("\nSolution:")
print(f"x = {x[0]}, y = {x[1]}, z = {x[2]}")
