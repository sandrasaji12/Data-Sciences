print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
array_id = np.array([1,2,3,4,5])
print("\n\n1D Array before insertion:")
print(array_id)

array_id = np.insert(array_id,2,6)
print("\n1D Array after insertion:")
print(array_id)

array_2d = np.array([[1,2,3],
                    [4,5,6]])
print("\nOriginal 2D array:")
print(array_2d)
array_id = np.insert(array_2d,1,[7,8,9], axis=0)
print("\n2D Array after insertion:")
print(array_2d)