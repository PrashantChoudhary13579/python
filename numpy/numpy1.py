import numpy as np

# Creating the array by passing the tuple
arr = np.array((1,2,3,4,5))
print (arr)
print(type(arr))

# Creating the array by passing the list
ar = np.array([3,5,7,9,11])
print(ar)
print(type(ar))

# Dimensions in an array also called rank of the array. (numpy.ndarray.ndim)

# 0-Dimension array
n = np.array(25)
print(n)
print("Dimensions = ",n.ndim)

# 1-Dimension array
print()
n1 = np.array([10,20,30])
print(n1)
print("Dimensions =",n1.ndim)

# 2 -Dimension array
print()
n2 = np.array([[10,20,30],[40,50,60],[80,90,100]])
print(n2)
print(n2.ndim,"dimension array ")

# Initialize numpy array 
# To initialize numpy arrays, we can use the numpy.zeros() method. using the method, initialize numpy arrays with zeros.

num = np.zeros([4,4])
print(num)
print(type(num))

# Data types in numpy - b-boolean, s - string,o - object, m - timedate, i - signed integer, u - unsigned integer, f - floating point.
print()
value = np.array([12,23,34])
print(value.dtype)

string = np.array(["hello","world","what's up"])
print(string)
print(string.dtype)


string = np.array(["hello","world","what's up"],dtype = 'S7')
print(string)
print(string.dtype)

# converting one data type to another
n = np.array([10,20,30,40])
print(n)
print(n.dtype)
n2 = n.astype('U')
print(n2)
print(n2.dtype)