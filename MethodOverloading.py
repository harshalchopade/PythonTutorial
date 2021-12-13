#In python we dont have method overloading concept.
#Python doesnt allow to have the methods with same name.

#In the below example addition() expecting 3 vars but we are passing only 2
#To work we can do

class Student:

    def addition(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s =a+b
        else:
            s = a

        return s

s1 = Student()
result = s1.addition(1)

print(result)