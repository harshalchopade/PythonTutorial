#Class
#Class is a design for the object.If we dont have the class how we can define the object.
#we cant keep the class empty if you want metion pass
#Define the class using below syntax:

#Object
#Inside class we can put attribute(variables) and behavior(methods).
class Class_Object:
    def config(self):
        print("i5, 16GB, 1TB")

#Approach1 to call methods after creation of object
#Object creation syntax is at line 11
object_1 = Class_Object()
Class_Object.config(object_1)

#Approach2
#here object_1 will be pssing as self object to config()
object_1.config()






