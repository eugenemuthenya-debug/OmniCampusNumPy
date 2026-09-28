# to import the library as a whole
# NumPy is a powerful library for numerical computing in python
# numpy.ndarray : is a multi-dimensional(1D,2D,3D) data structure that can hold elements of same data type
import numpy as np

# converting python lists into a numpy.ndarray using:
# np.ndarray()[n-dimensional array(n=1,2,3 dimension)]
# python list--> using []
a = [1,2,3,4,5]
b = [6,7,8,9,10]
# print (a)

# convert it into np.ndarray and store in a new variable
a = np.array(a)
b = np.array(b)
print("a:",a)
print("b:",b)

# check the type using type() function
print("type a",type(a))
print("type b",type(b))

# we can convert back to python list using.tolist() function
a_list = a.tolist()
print(a_list)
print(type(a_list))

# Homogenous:All elements are of the same type of numpy.ndarray()
# Efficient:Designed for performing numerical computations
# Flexible : Support slicing,indexing and advanced operations.



