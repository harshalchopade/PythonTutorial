#Type of vars
#1.Instance vars
#2.Class vars (static var)

#Instance Vars
#If we define the var inside __init__.eg mil, comp
#Class vars
#If we define the var outside __init__ and inside a class its a class vars.eg wheels

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.comp = 'BMW'

#Here mil and comp are instance vars because as the car (object) changes it will change.
#We can change the values of the variables for the object using following way

c1 = Car()
c2= Car()

c2.mil = 20 #changing the mil var value for object2 ie c2

print(c1.comp, c1.mil, c1.wheels) # accessing instance var using object name same apply to class var
print(c2.comp, c2.mil, Car.wheels) #we can access class var using class name as well.
