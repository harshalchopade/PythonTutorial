#Instance Methods


class Student:
    school_name = "ABC"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchoolName(cls):
        return cls.school_name

    @staticmethod
    def info():
        print("This is student class in ABC module.")

#Here avg() is a instance method as you can it work with object (self)
#But instance method is having 2 types
#Accessor - only fetching the value of instance vars. #getter method
#Mutator - to modify the value of instance vars. #setter method
#Here m1 ,m2 are instance vars, it can be used with instance methods.
s1 = Student(32,45,65)
s2 = Student(45,7,58)

print(s1.avg())
print(s2.avg())

#Class methods
#school is a class var to use that we need to have class methods.
#As we are working with class var we need to use (cls) instead of (self)
#Here to call class methods we can use objects, but is should be for every object so we use class name to call method
#To indicate class method use @classmethod decorator.

print(Student.getSchoolName())


#Static Methods
#The method which nothing to do with any type of vars so then go for static methods
#If we want to perofm any operation with other calss object so that we can use this.
Student.info()