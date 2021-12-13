#Global Keyword
#When it comes to functions and variables we can create variables inside function, also outside function as well.
#That where concept comes into the picture called scope.

a=10
def something():
    a= 15
    b=55
    print(a)

print(a)
#print(b)
#In the above eg we have two variable with same name 'a' yes it is possible if both have different scope.
#Outside 'a' is called global var.
#Var 'a' inside something() called local var, which means we can not use this var outside fn.in our eg 'b'.

a=10
def something():
    a= 15
    print("in fn: ", a)

something()
print("outside fn: ", a)

#o/p
#in fn:  15
#outside fn:  10

#In above code,o/p in fn:  15 which means the local var inside the function preference given to local var
#Outside is 10 because we cant access local var outside.

########################################################################
#In below example its shows that we can access global variable inside the function directly.
a=10
def something():
    print("in fn: ", a)

something()
print("outside fn: ", a)

#o/p
#in fn:  10
#outside fn:  10

#But what if I change the value of a = 15 inside function, but is it local var or global var as we are changing it
#that where the problem starts, till that we are thing global var, but I want to chnage the var of global var now.
#To chnage it, we if we want to specify the inside 'a' we are using is not a local variable it is a global var
#In that case we need to mention explicitly global 'a'
#This is where are specifying to python,my intention here to use global var not local var.

a = 10
def something():
    global a
    a = 15
    print("in fn: ", a)

something()
print("outside fn: ", a)

#o/p
#in fn:  15
#outside fn:  15

#Here the outside 'a' value is also 15 because the change is not on local var as we are not having local var.
#If we want to use global var we need to use global keyword.

#But here also we have a problem, if we say global 'a' that means this function has var 'a' now and if we want to create
#another var 'a' we cant do that.
#We can not have global and local var 'a' in the same function now.

a = 10
def something():
    global a
    a = 15
    print("in fn: ", a)
    a = 9

something()
print("outside fn: ", a)

########################################################################
#To have local and global in the same function
#To do that we have touse globals() to access the address of global vars  and it will return all the global vars.
#If you want to change the gloabl var value from function without affecting the local var i.e when local and global var
#names are same within the function.
a = 10
print(id(a))
def something():
    a = 9
    x = globals()['a'] # to specify the var you want to access
    print(id(x))
    print("in fn: ", a)
    globals()['a'] = 15


something()
print("outside fn: ", a)

#o/p
#1369712558608
#1369712558608
#in fn:  9
#outside fn:  15