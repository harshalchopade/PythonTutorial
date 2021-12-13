#To create an empty array and then user pass the length and values for the array
#Store the user entered value and print it
from array import *
arr = array('i', [])
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input(("Please enter the next value :")))
    arr.append(x)

for j in arr:
    print(j)

#To get the index of array element

m = 0
n = int(input("Enter the number whose index to be find: "))
for l in arr:
    if n==l:
        m+=1
        break

print("The index of the given no is ", m)

print(arr.index(n))