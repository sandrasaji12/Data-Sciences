print("SJC23MCA-2047 : SANDRA SAJI")
print("Batch : MCA 2023-25")

import numpy as np
x = np.array([[1,2],
              [3,4]])
y = np.random.rand(*x.shape)
result = x * 2 + 2 * y
print(result)