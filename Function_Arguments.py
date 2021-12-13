#Function Arguments

def update(x):
    x = 8
    print("Value of x is: ", x)

update(10)

#In the above example we are accepting the value 10 in x and then in update() we are updating x value to 8
#So values of x gets updated while printing.

#Now in below example instead of passing value directly we create variable and assign value then pass it to fn
#

def update(x):
    x = 8
    print("Value of x is: ", x)

a = 20
update(a)
print("Value of x is: ", a)

#In above example even if we updating the value of x it will not affect the value of a.

#Call By Value
#Whenever we are calling a function by passing a variable value it will be pass as a value
#In above eg update(a) we are not passing 'a' we are passing 10.
#In pass by value we are passing the value not the address.
#When we pass the value whatever happens with the value 'a' is not concerned about it because the moment we pass the
#value it will create a different memory i.e 'x' will get different memory of 10
#So even if you update that 10 value it will not affect that 'a' value.

#Pass By Ref
#We pass address here which means we are not passing 10 we are passing the addrss of 'a' which means we change the value
#of 'x' will affect the value of 'a'.

#In python we dont have any concepts #hahaha

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("Value of x is: ", x)

a = 20
print(id(a))
update(a)
print("Value of x is: ", a)

#Note
#Whenever we are calling a function by passing a value/variable they will share the id i.e refering to same object
#i.e the var which you passed 'a' and var you are accessing ('x')
#But if you chnage the value it will change the address.
#When you update the value it will create the new memory because int, string are immutable.

#mutable types will share same id


def update(lst):
    print(id(lst))
    lst[1] = 10
    print(id(lst))
    print("Value of lst is: ", lst)

lst = [1,2,3,4]
print(id(lst))
update(lst)
print("Value of lst is: ", lst)
