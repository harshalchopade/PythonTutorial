#you can create object of inner class inside the outer class
#or
#you can create the inner class object outside outer class provided you use the outer class name to call it.
class student:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        #self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.name = 'Lenovo'
            self.pro = 'i5'
            self.ram = '8'

        def show(self):
            print(self.name, self.pro, self.ram)


s1 = student('Harsha', 2)
s2 = student('Akshaya',3)

s1.show()

#Object Creation

#lap1 = s1.lap
#lap2 = s2.lap

#or

#Outside class
#lap1 = Student.Laptop()
