# Array indexing - we will learn about the indexing done in the array 1st element at 1st index and so on..
import numpy as np

# Accessing elements in 1D array
n = np.array([12,23,34,45,46,67,78])
print(n)
print(n[0])
print(n[1])
print(n[2])
print(n[3])

# Accessing elements in 2D array
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Printing complete array
print(d)
# Print the each row 
print(d[0])
print(d[1])
print(d[2])
# Print the specific element
print(d[0,0])
print(d[1,1])
print(d[2,2])

# Accessing the elements from the 3D array
v  = np.array([[[5,10,15],[20,25,30]],[[35,40,45],[50,55,60]]])
# Printing the whole array
print(v)

# Printing the specific element
print(v[0,0,0])
print(v[0,0,1])
print(v[0,0,2])

# Printing the whole row
print(v[0,1])
print(v[1,0])
print(v[1,1])

# Printing the complete plane
print(v[0])
print(v[1])

# Accessing Negative indexing 
print("Last element =",n[-1])
print("Second Last element =",n[-2])
print("Out of bound element =",n[-7])


print("Element in 2D")
print("Last element in 2d = ",d[0,-1])
print("Last element in 2d = ",d[-1,-1])
print("Last element in 2d = ",d[2,-1])

# Array slicing 
# - it means that we slice the array in a range from starting to the end . The slice/range is passed in place of the index eg - n[1:3]
nval = np.array([5,10,12,23,34,4,56,76,87,89])
print(nval[2:6])
print(nval[5:])
print(nval[:4])
print(nval[1:10:2])

# slicing a 2D array 
n = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(n[0,2:4])
print(n[0:2,2:4])

# Array shape - no. of elements in each dimension
# numpy.shape
# 0 dimesion array
shape0 = np.array(10)
print(shape0)
print(shape0.ndim)
print(shape0.shape)
# 1 dimension array
shape1 = np.array([10,20,30,40,50,60])
print(shape1)
print(shape1.ndim)
print(shape1.shape)
# 2 dimension array
shape2 = np.array([[10,20,30,40],[30,40,50,60]])
print(shape2)
print(shape2.ndim)
print(shape2.shape)

# 3 dimension array
shape3 = np.array([[[10,20,30,40],[30,40,50,60],[10,20,30,40]],[[10,20,30,40],[30,40,50,60],[10,20,30,40]],[[10,20,30,40],[30,40,50,60],[10,20,30,40]]])
print(shape3)
print(shape3.ndim)
print(shape3.shape)
