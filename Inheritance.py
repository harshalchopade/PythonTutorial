#Single Level Inheritance

class A:

    def feature1(self):
        print("Feature1 working")

    def feature2(self):
        print("Feature2 working")

class B(A):
    def feature3(self):
        print("Feature3 working")

    def feature4(self):
        print("Feature4 working")

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

#MultiLevel Inheritance
class C(B):
    def feature5(self):
        print("Feature5 working")

    def feature6(self):
        print("Feature6 working")

c = C()
c.feature3()

class D():
    def feature7(self):
        print("Feature7 working")

    def feature8(self):
        print("Feature8 working")


#Multiple Inheritance
class E(C,D):
    def feature7(self):
        print("Feature7 working")

    def feature8(self):
        print("Feature8 working")

e = E()
e.feature1()
e.feature3()
e.feature5()