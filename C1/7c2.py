print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
matrix1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrix2 = np.array([[9,8,7], [6,5,4], [3,2,1]])
matrix_sum = matrix1 + matrix2
matrix_diff = matrix1 - matrix2
matrix_product = matrix1 * matrix2
matrix_divide = matrix1 / matrix2
matrix_multiply = np.dot(matrix1,matrix2)
matrix_transpose = np.transpose(matrix1)
diagonal_sum = np.trace(matrix1)
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix sum:\n", matrix_sum)
print("Matrix difference:\n", matrix_diff)
print("Matrix element-wise product:\n", matrix_product)
print("Matrix element-wise division:\n", matrix_divide)
print("Matrix multiplication:\n", matrix_multiply)
print("Transpose of matrix 1:\n", matrix_transpose)
print("Sum of diagonal elements of matrix 1:\n", diagonal_sum)

