print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
x = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
x_cube_multiply = np.multiply(x, np.multiply(x, x))
x_cube_operator = x * x * x
x_cube_power = np.power(x,3)
x_cube_double_star = x ** 3
identity_matrix = np.identity(x.shape[0])
x_power_2 = np.power(x,2)
x_power_3 = np.power(x,3)
x_power_4 = np.power(x,4)

print("Original matrix x:")
print(x)
print("\nCubed matrix (Method 1 - multiply()):")
print(x_cube_multiply)
print("\nCubed matrix (Method 2 - * operator):")
print(x_cube_operator)
print("\nCubed matrix (Method 3 - power()):")
print(x_cube_power)
print("\nCubed matrix (Method 4 - ** operator):")
print(x_cube_double_star)
print("\nIdentity matrix:")
print(identity_matrix)
print("\nMatrix to different powers:")
print("x^2:")
print(x_power_2)
print("\nx^3:")
print(x_power_3)
print("\nx^4:")
print(x_power_4)

