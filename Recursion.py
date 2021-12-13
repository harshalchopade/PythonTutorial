#Recursion
#A function calling itself
#By default limit is 1000 times
#If you want to change use below steps

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000) #to set recursion limit

i=0
def greet():
    global i
    i+=1
    print("Hello ", i)
    greet()

#greet()


###############################################################################
#Factorial of a number using recursion

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

print(fact(5))