print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
A = np.array([[5,27,32],[14,53,62],[67,88,19]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt
print("Original matrix A:")
print(A)
print("\nSingular values:")
print(S)
print("\nReconstructed matrix A_hat:")
print(A_hat)