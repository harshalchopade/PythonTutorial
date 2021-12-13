from numpy import *
arr = array([1,2,3,4,5,45,8,9])

#To find the size of an array
print(arr.size)

#To find max element from array
print(arr.max())

#To find min element from array
print(arr.min())

#To put the value at specified index by overriding the exisitng value
arr.put(2,50)
print(arr)

#To sort the array
arr.sort()
print(arr)

#To add 5 in each element of an array
arr = arr + 5
print(arr)

#To add two different arrays then no element should be same
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

sum = arr1+arr2
print(sum)

#To find sin values of an array
print(sin(arr))

#To find sqrt of an array
print(sqrt(arr))

#To find unique element of an array
print(unique(arr))

#To concentate two array
print(concatenate([arr1,arr2]))

#Copy an array - approach1
marks_1 = array([1,2,3,4,5])
marks_2 = marks_1
print(marks_1)

#In this example we are copying marks_1 to marks_2 at line 46.
#But actually its not copying the array it just aliasing with different name
#Both marks_1 and marks_2 will be poitning to same array.
print(id(marks_1))
print(id(marks_2))

#Copy an array - approach2 - Shallow copy
marks_2 =marks_1.view()
print(id(marks_1))
print(id(marks_2))
#Here if you see address will be different i.e means two array gets created.
#But here also small problem is there, as we are uisng view() so it will be doing shallow copy
#It means it will copy the element but still both arrays will be dependent on each other.
#If we change the element in array it will affect both the arrays
marks_2[0] = 10
print(marks_1)
print(marks_2)

#Copy an array - approach3 - Deep copy
marks_2 =marks_1.copy()
print(id(marks_1))
print(id(marks_2))
#If we change the element in array it will not affect both the arrays
print(marks_1)
print(marks_2)

#maximum element form array
# Initialize array
arr = [25, 11, 7, 75, 56];
# Initialize max with first element of array.
max = arr[0];
# Loop through the array
for i in range(0, len(arr)):
    # Compare elements of array with max
    if (arr[i] > max):
        max = arr[i];
print("Largest element present in given array: " + str(max));