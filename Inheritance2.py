import Inheritance

class B(Inheritance.A):
    def feature3(self):
        print("Feature3 working")

b = B()
b.feature1()
b.feature2()
b.feature3()