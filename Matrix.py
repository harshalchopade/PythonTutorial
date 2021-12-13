from numpy import *

#To create multi dimensional array using following syntax.
arr = array([
               [1,2,3,4,5,6],
               [7,8,9,10,11,12]
            ])
print(arr)

#To know type of data you are working
print(arr.dtype)

#To find dimension of the array
print(arr.ndim)

#To find no of rows and no of cols
print(arr.shape)

#To find size of the total block
print(arr.size)

#To convert 2D array to 1D array
arr1 = arr.flatten()
print(arr1)

#To convert 1D array to 2D array
arr2 =arr.reshape(3,4) #Three rows and four columns
print(arr2)

#To convert 1D array to 3D array
arr2 =arr.reshape(2,2,3) #Three rows and four columns
print(arr2)

#Matrices
#To convert the array into matrix

m = matrix(arr)
print(m)

n = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
print(n)

#To find diagonal of matrix
print(diagonal(n))

#To find min value from matrix
print(n.min())

#To find multiplication of matrix
m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

result = m1 * m2
print(result)
