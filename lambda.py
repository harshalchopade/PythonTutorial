#Lambda
#We know how to define function till now, But I dont mention fn name called as Anonymous Functions
#or also called as lambda

def square(a):
    return a*a

print(square(5))

#In above example we have fn defination
#We have only one expression which is returning value
#But we are using two line def and return statment
#But what I want to use function only once and I dont want to define the name of fn and have only one expression
#We can pass function to function as it is object.

f = lambda a: a*a
result = f(5)
print(result)
#Here 'a' is an args we are passing and the operation on that arg is a*a
#We need to use lambda keyword to define Anonymous fn.
#To use that fn we need to store in some vars.

#Let's say I want to add two nos to pass multiple args to lambda
#Point to remember here is that we can pass any of args but it should be only of expression(+,-,*,/ etc)
f = lambda a,b: a+b
result = f(5,7)
print(result)