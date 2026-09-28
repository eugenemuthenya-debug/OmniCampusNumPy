# import numpy
import numpy as np
# Broadcasting->(when performing a universal binary operation on two arrays with different  lengths,one of the arrays is automatically broadcast to match the other in terms of dimension and length.)
a = np.array([1,2,3])
print("2a =", 2* a)

twos = np.array([2,2,2])
print("2a =",twos * a)

# Performing on two 1-dimensional arrays
b = np.array([1,2,3,4,5])
c = np.array([1,2])
# print("b + c:", b+c)
# This raises an error due to shape mismatch.
# Length must be in 1 order for numpy to repeat and match length,if not 1 numpy cannot automatically broadcast the array.

