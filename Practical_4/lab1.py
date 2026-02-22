import numpy as np

# 4x4 Identity matrix
print("Identity 4x4:\n", np.eye(4), "\n")

# Two 3x3 random matrices, addition & multiplication
a, b = np.random.randint(1, 10, (3,3)), np.random.randint(1, 10, (3,3))
print("Matrix 1:\n", a)
print("Matrix 2:\n", b)
print("Addition:\n", a+b)
print("Multiplication:\n", a@b)