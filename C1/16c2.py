print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.array([-3,5,-2])
x = np.linalg.solve(A,b)
print("Matrix A:")
print(A)
print("Vector b:")
print(b)
print("Solution for x:")
print(x)