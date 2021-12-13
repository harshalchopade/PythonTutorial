#What is function
#It is block of code which contains the statment that we need to use repetatively.
#Code reusability, maintainance is easy.
#Instead of developing large code we can use chunks of the code which help to understand ,modification
#To create a function follow below syntax
# def name_of_fn():
#  statment1
#  etc

#After creating the function we also need to call explicitly.o/w it will not execute.
#Define it once call it multiple times.


def greet():
    print("Hello!")
    print("Welcome to DISNEY WORLD.")

greet()

#Function can accepts paramters/arguments
def add(a:int, b:int):
    c = a+b
    print("The addition of two number is: ", c)

add(4,5)

#Function can return values as well so we can store in some variable and then use in the rest of code.
#To return any we have to use 'return' keyword
def add(a:int, b:int):
    c = a+b
    return c

result = add(4,5)
print("The result returned by the add function is :", result)

#Also we can return mutliple values form function
def add_sub(a:int, b:int):
    c = a+b
    d = a-b
    return c, d

result1, result2 = add_sub(4,5)
print("The result1 returned by the add function is :", result1)
print("The result1 returned by the sub function is :", result2)