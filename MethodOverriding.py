class A:
    def show(self):
        print("In class A")

class B(A):
    def show(self):
        print("In class B")


a1 = B()
a1.show()

