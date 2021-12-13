#Different ways to create array using nump

#1.using array()
from numpy import *
arr = array([1,2,3,4,5])
print(arr)  #[1 2 3 4]
print(arr.dtype) # to check type of array

#If I add float value in above array then all the values of arrays converted into float.
#But array should have the homogenous data but while using numpy it will allow to put different type of values.
#Python implicitly conversion did this.

arr = array([1,2,3,4,5.0])
print(arr) #[1. 2. 3. 4. 5.]

#If I specify the type as int then all values will be converted to int
arr = array([1,2,3,4,5.0], int)
print(arr) #[1 2 3 4 5]

#Similarly If I specify int values and mention the type as float then all values will be converted to float
arr = array([1,2,3,4,5.0], float)
print(arr) #[1. 2. 3. 4. 5.]

#2.linspace()
arr = linspace(0,15,2)
#here first paramter is start of seq
#2nd is stop of seq (inclusive)
#3rd is number of parts i want to go for i.e it will break the 0 to 15 into 16 parts
#o/p should be in float as we are dviding in the parts.
#If we dont specify third elemnt then it will break by defualt in 50 parts.
#Here diff b/w two element will be same.
print(arr) #[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]

#3.arange()
arr = arange(1,15,2)
#here first paramter is start of seq
#2nd is stop of seq (exclusive)
#3rd is step
print(arr)

#4.arange()
arr = logspace(1,40,5)
#Here diff b/w two element will be depending upon the log of it
#It will start from 10^1 to 10^40

print('%.2f' %arr[4])

#5.zeros()
#When we need to create array with all the values should be 0
#By default will get float in o/p but we wont mention int use below syntax
arr = zeros(5, int)
print(arr)

#5.ones()
#When we need to create array with all the values should be 0
#By default will get float in o/p but we wont mention int use below syntax
arr = ones(5, int)
print(arr)