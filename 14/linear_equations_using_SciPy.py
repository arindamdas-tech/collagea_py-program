import numpy as np
from scipy.linalg import solve

# Define the coefficient matrix A and the constant vector b
A = np.array([
    [2, 3],
    [4, 5]
])

b = np.array([8, 14])

# Solve the system of linear equations Ax = b
solution= solve(A, b)
x=solution[0]
y=solution[1]

print("value of x:", x)
print("value of y:", y)