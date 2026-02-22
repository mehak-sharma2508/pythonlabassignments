import numpy as np

# Input 5x3 matrix
print("Enter 15 numbers for 5x3 matrix (space-separated):")
A = np.array([int(x) for x in input().split()]).reshape(5, 3)

# Input 3x2 matrix
print("Enter 6 numbers for 3x2 matrix (space-separated):")
B = np.array([int(x) for x in input().split()]).reshape(3, 2)

# Multiply matrices
C = A @ B

print("5x3 Matrix:\n", A)
print("3x2 Matrix:\n", B)
print("Product Matrix (5x2):\n", C)