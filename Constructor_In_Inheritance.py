#In python when if we have constructor in parent and child class both then only child class constr gets executed
#If child class dont have the constructor then only parent class constructor gets executed.
#But if we want to parent and child class constructor both then use super().__init__()
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature1 working")

    def feature2(self):
        print("Feature2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature3(self):
        print("Feature3 working")

    def feature4(self):
        print("Feature4 working")

#a = A()
b= B()

#Here i.e in mutliple inheritance first it will find the init of itself then it call super()
#But after that super() of left to right class here i.e A #Method resolution order
#Also if classA and classB having same method, while calling MRO will be executed and based on that methods gets called
class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C init")

    def feat(self):
        super().feature2()
        
    def feature5(self):
        print("Feature5 working")

    def feature6(self):
        print("Feature6 working")

c = C()
