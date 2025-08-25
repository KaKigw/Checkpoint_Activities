import numpy as np
# 1D Array
array_1D = np.array([10, 11, 12, 13, 14])
# 2D Array
array_2D = np.array([[20, 30, 40, 50, 60], [43, 54, 65, 76, 87], [11, 22, 33, 44, 55]])
# 3D Array
array_3D = np.array([[[1, 2, 3, 4, 5], [11, 21, 31, 41, 51]], [[11, 12, 13, 14, 15], [51, 52, 53, 54, 5]]])


""" 
Display the first element (not necessarily individual element) for each of the 3 arrays we defined above
Call the first individual element of the each of the 3 arrays.
Uses negative indices to display the last element of each array
 """

print(array_1D[0])
print(array_2D[0])
print(array_3D[0])
print("\n")
print(array_1D[0])
print(array_2D[0,0])
print(array_3D[0,0,0])
print("\n")
print(array_1D[-1])
print(array_2D[-1,-1])
print(array_3D[-1,-1,-1])

"""Given array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), what will this slicing operation return?"""
import numpy as np
array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array3[1:8:2])

print(np.__version__)
np.show_config()

Z = np.zeros(10)
print(Z)

Z = np.arange(10,50)
print(Z)