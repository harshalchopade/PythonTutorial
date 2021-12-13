#By default python doesnt support abstract concept
#The workaround is to use abstact base class module
#Abstarct methods have only method declaration but not having method defination/body.
#The class which having abstract method is called abstract class.But as we discussed python dont support abstraction
#To declare class as abstract we have import ABC, abstractmethod

#Summary:
#abstract method is a method which only has declaration and doesn't have definition.
#a class is called abstract class only if it has at least one abstract method.
#when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
#if it is not done then child class also becomes abstract class automatically.
#at last, python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract.


from abc import ABC, abstractclassmethod

class Computer:
    @abstractclassmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Hello lets process")

l1= Laptop()
l1.process()