import numpy as np

# Coefficient matrix
A = np.array([
    [1, -1],
    [1,  1]
])
# Constant matrix
B = np.array([1, 11])

# Solve the equations
solution = np.linalg.solve(A, B)

x = solution[0]
y = solution[1]

print("Velocity of Car 1 =", x)
print("Velocity of Car 2 =", y)