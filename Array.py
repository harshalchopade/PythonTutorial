#Array can be used when we have homogenous data with us.
#Array in python is dynamic in size.
#Arrays can be accessed using index.
#To use array we need to import array module
#While creating array we need to specify data type and values of the array
#To define array data type we need to use typecode

#Note:
# 'b' - signed char
# 'B' - unsigned char
# 'i' - signed int
# 'I' - unsigned int

import array as arr
# from array import *
vals = arr.array('i',[1,2,3,4])
print(vals)

#if we put different value like add float value will get error
#vals = arr.array('i',[1,2,3,4.5])

#To get the size of array we need to below function
print(vals.buffer_info()) # it will return two parameters first is address and second is size of the array.

#To get the array type
print(vals.typecode)

#To add elements into the arry
vals.append(6)
print(vals)

#To remove elements into the arry
vals.remove(6)
print(vals)

#To reverse the array
vals.reverse()
print(vals)

#To print the value one by one
for i in range(len(vals)):
    print(vals[i])

#Another approach to print the values
for j in (vals):
    print(j)

#Another approach to print the values
m = 0
while m<len(vals):
    print(vals[m])
    m+=1

#To create new array using exisitng array
#in the below example we are getting type of array using typecode and then we are saying fetch value one by one
#from previous array and store in a
marks = arr.array(vals.typecode, [a for a in vals])
#print(marks)

#To sort the array
sorted(marks)
print(marks)

#Another approach to sort

values = arr('i', [5,9,1,10,23])
for i in range(len(values)):
    j = i+1
    for j in range(len(values)):
        if (values[i]<values[j]):
            temp = vals[i]
            values[i] = values[j]
            values[j] = temp
for i in range(len(values)):
    print(values[i])

#To work with character
char = arr.array('u', ['a','e', 'i', 'o', 'u'])
print(char)