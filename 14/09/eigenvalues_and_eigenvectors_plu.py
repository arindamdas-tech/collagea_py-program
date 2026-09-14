import numpy as np
from scipy.linalg import lu

# Create a 4 x 4 square matrix
A = np.array([
    [4, 2, 1, 3],
    [3, 5, 2, 1],
    [1, 2, 4, 2],
    [2, 1, 3, 6]
], dtype=float)

print("Matrix A:")
print(A)

# i) Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# ii) PLU Decomposition
P, L, U = lu(A)

print("\nPermutation Matrix P:")
print(P)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

# Verification
print("\nVerification: P @ L @ U")
print(P @ L @ U)